#!/usr/bin/env python3
"""Turns activities/scratch/*/<name>.json (blocks + variables) into <name>.sb3 with Mobsya's Scratch.

Needs: launcher/webapps (fetch-webapps.sh), node (test/mock-tdm.cjs), Python Playwright and Chrome.
Each project is loaded into Scratch's virtual machine and saved by Scratch itself, so the .sb3 is
exactly what Scratch would write; the script then reloads it and checks the blocks are all there.
Run from launcher/:  python3 tools/build_sb3.py
"""
import asyncio, base64, glob, json, os, subprocess, sys, time
from playwright.async_api import async_playwright

FIND_VM = open(os.path.join(os.path.dirname(__file__), 'find-scratch-vm.js')).read()
URL = 'http://127.0.0.1:8766/scratch/index.html?device=%7B11111111-2222-4333-8444-555555555555%7D&ws=ws%3A%2F%2F127.0.0.1%3A8597&pass='
CHROME = os.environ.get('CHROME', '/usr/bin/google-chrome')


async def main():
    files = sorted(glob.glob('activities/scratch/*/*.json'))
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        page = await browser.new_page(viewport={'width': 1300, 'height': 800})
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        await page.goto(URL)
        await page.wait_for_timeout(6000)
        await page.evaluate('window.__vm = ' + FIND_VM)
        base = await page.evaluate('window.__vm.toJSON()')
        failed = 0
        for f in files:
            data = json.load(open(f))
            proj = json.loads(base)
            sprite = next(t for t in proj['targets'] if not t['isStage'])
            sprite['blocks'] = data['blocks']
            sprite['variables'] = data['variables']
            proj['extensions'] = ['thymio']
            b64 = await page.evaluate('''async (text) => {
                await window.__vm.loadProject(text);
                const blob = await window.__vm.saveProjectSb3();
                const buf = new Uint8Array(await blob.arrayBuffer());
                let s = ''; for (const c of buf) s += String.fromCharCode(c);
                return btoa(s);
            }''', json.dumps(proj))
            out = f[:-5] + '.sb3'
            open(out, 'wb').write(base64.b64decode(b64))
            # reload the saved file and compare the blocks
            back = await page.evaluate('''async (b64) => {
                const bin = atob(b64); const buf = new Uint8Array(bin.length);
                for (let i = 0; i < bin.length; i++) buf[i] = bin.charCodeAt(i);
                await window.__vm.loadProject(buf.buffer);
                const t = JSON.parse(window.__vm.toJSON()).targets.find((x) => !x.isStage);
                // Scratch stores variable reporters inside inputs as [12, name, id]: count them separately.
                const list = Object.values(t.blocks).filter((b) => !Array.isArray(b)).map((b) => [b.opcode, JSON.stringify(b.fields)]);
                const vars = JSON.stringify(t.blocks).split('[12,').length - 1;
                return { list, vars };
            }''', b64)
            want = sorted([b['opcode'], json.dumps(b['fields'], separators=(',', ':'))] for b in data['blocks'].values() if b['opcode'] != 'data_variable')
            want_vars = sum(1 for b in data['blocks'].values() if b['opcode'] == 'data_variable')
            got = sorted([o, json.dumps(json.loads(fl), separators=(',', ':'))] for o, fl in back['list'])
            ok = want == got and back['vars'] == want_vars and not errors
            failed += not ok
            print('OK  ' if ok else 'FAIL', out, f'{len(got)} blocks + {back["vars"]} variable reporters', errors[:2] if errors else '')
            if not ok and want != got:
                print('   missing:', [w for w in want if w not in got][:5], 'extra:', [g for g in got if g not in want][:5])
            errors.clear()
            os.remove(f)
        await browser.close()
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))
    mock = subprocess.Popen(['node', 'test/mock-tdm.cjs'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    http = subprocess.Popen([sys.executable, '-m', 'http.server', '8766'], cwd='webapps', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)
    try:
        asyncio.run(main())
    finally:
        mock.terminate(); http.terminate()
