# Writes activity.<lang>.md for es, pl, ar, he, zh, ja (same format as /home/claude/tr/w.py).
import os, re, sys
sys.path.insert(0, '/home/claude/tr')
from w import write, front, ROOT
ADAPT = {'es': 'adaptado por Mobsya', 'pl': 'adaptacja Mobsya', 'ar': 'بتكييف من Mobsya',
         'he': 'בעיבוד Mobsya', 'zh': 'Mobsya 改编', 'ja': 'Mobsya による翻案'}
AND = {'es': 'y', 'pl': 'i', 'ar': 'و', 'he': 'ו', 'zh': '和', 'ja': '、'}
TS = {'es': 'Actividades de Thymio Suite', 'pl': 'Aktywności Thymio Suite', 'ar': 'أنشطة Thymio Suite',
      'he': 'פעילויות Thymio Suite', 'zh': 'Thymio Suite 活动', 'ja': 'Thymio Suite のアクティビティ'}
VPL3 = {'es': 'Guía docente de VPL3 de la EPFL (Mobots) y la HEP-Vaud, adaptada por Mobsya',
        'pl': 'Przewodnik dla nauczyciela VPL3, EPFL (Mobots) i HEP-Vaud, adaptacja Mobsya',
        'ar': 'دليل المعلّم لـ VPL3 من EPFL (Mobots) وHEP-Vaud، بتكييف من Mobsya',
        'he': 'מדריך למורה של VPL3 מאת EPFL (Mobots) ו-HEP-Vaud, בעיבוד Mobsya',
        'zh': 'VPL3 教师指南，EPFL (Mobots) 与 HEP-Vaud 编写，Mobsya 改编',
        'ja': 'EPFL (Mobots) と HEP-Vaud による VPL3 教師用ガイド（Mobsya による翻案）'}
Q = {'es': ('«', '»'), 'pl': ('„', '”'), 'ar': ('«', '»'), 'he': ('"', '"'), 'zh': ('《', '》'), 'ja': ('『', '』')}
def author(en, lang):
    if en == 'Thymio Suite activities': return TS[lang]
    if en.startswith('VPL3 teacher guide'): return VPL3[lang]
    m = re.match(r'(.*?), "(.*?)" \((.*?)\), adapted into English', en)
    assert m, en
    who, book, pub = m.groups()
    who = who.replace(' and ', {'he': ' ו-', 'ar': ' و', 'zh': ' 和 ', 'ja': '、'}.get(lang, f' {AND[lang]} '))
    a, b = Q[lang]
    sep = '，' if lang in ('zh',) else '、' if lang == 'ja' else '، ' if lang == 'ar' else ', '
    return f'{who}{sep}{a}{book}{b} ({pub}){sep}{ADAPT[lang]}'
def W(folder, lang, **k):
    meta, _ = front(os.path.join(ROOT, folder, 'activity.md'))
    k['author'] = author(meta['author'].strip(), lang)
    write(folder, lang, k)
