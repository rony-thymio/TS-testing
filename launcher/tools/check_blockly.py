#!/usr/bin/env python3
"""Opens every activities/blockly/*/solution.aesl in Thymio Blockly (through the activity loader),
reads the Aseba code Blockly generates, checks it, and stores it in the .aesl file (as Blockly's
own Save does). Prints the code so it can be reviewed.
Needs launcher/webapps (fetch-webapps.sh), node, Python Playwright and Chrome.
Run from launcher/:  python3 tools/check_blockly.py
"""
import asyncio, glob, os, shutil, subprocess, sys, time
from xml.sax.saxutils import escape
from playwright.async_api import async_playwright

CHROME = os.environ.get('CHROME', '/usr/bin/google-chrome')
URL = ('http://127.0.0.1:8766/thymio_blockly/thymio_blockly.en.html#device=%7B11111111-2222-4333-8444-555555555555%7D'
       '&ws=ws%3A%2F%2F127.0.0.1%3A8597&pass=&activity=')


async def main():
    failed = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        for f in sorted(glob.glob('activities/blockly/*/solution.aesl')):
            os.makedirs(os.path.dirname('webapps/' + f), exist_ok=True)
            shutil.copy(f, 'webapps/' + f)
            page = await browser.new_page(viewport={'width': 1200, 'height': 800})
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            await page.goto(URL + f.replace('/', '%2F'))
            await page.wait_for_timeout(3000)
            code = await page.evaluate("document.getElementById('importExport').value")
            name = f.split('/')[2]
            await page.screenshot(path=f'/tmp/blockly-{name}.png')
            await page.close()
            ok = bool(code.strip()) and 'undefined' not in code and not errors
            failed += not ok
            print(('OK  ' if ok else 'FAIL'), name, errors[:2])
            print('    ' + code.strip().replace('\n', '\n    '))
            text = open(f, encoding='utf-8').read()
            if '__CODE__' in text:
                open(f, 'w', encoding='utf-8').write(text.replace('__CODE__', escape(code.strip())))
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
