import pykakasi
from num2words import num2words
import re

def transliterate_japanese(text, style='standard', number_style='keep'):
    punctuation = {
        '、': ',',
        '。': '.',
        '？': '? ',
        '！': '! ',
    }

    long_vowels = {
        'aa': 'ā',
        'ee': 'ē',
        'ii': 'ī',
        'oo': 'ō',
        'uu': 'ū'
    }

    if not text:
        return ""

    kks = pykakasi.kakasi()

    kks.setMode("J", "a")
    kks.setMode("H", "a")
    kks.setMode("K", "a")

    if style == 'standard':
        kks.setMode("r", "Hepburn")
    elif style == 'hepburn':
        kks.setMode("r", "Hepburn")
    elif style == 'kunrei':
        kks.setMode("r", "Kunrei")
    elif style == 'passport':
        kks.setMode("r", "Passport")

    if number_style == 'words':
        def num2word(m):
            return num2words(int(m.group()), lang='ja')
        text = re.sub(r'\b\d+\b', num2word, text)

    kks.setMode("s", True)

    converter = kks.getConverter()
    output = converter.do(text)

    for exception, replacement in punctuation.items():
        output = output.replace(exception, replacement)

    if style == 'standard':
        for exception, replacement in long_vowels.items():
            output = output.replace(exception, replacement)

    return output