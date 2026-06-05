import re
from ifranlp.hebrew import language
from num2words import num2words

def transliterate_hebrew(text, number_style='keep'):
    hebrew_transliteration = {
        'א': "'",
        'ב': 'v',
        'ג': 'g',
        'ד': 'd',
        'ה': 'h',
        'ו': 'v',
        'ז': 'z',
        'ח': 'kh',
        'ט': 't',
        'י': 'y',
        'כ': 'kh',
        'ך': 'kh',
        'ל': 'l',
        'מ': 'm',
        'ם': 'm',
        'נ': 'n',
        'ן': 'n',
        'ס': 's',
        'ע': "'",
        'פ': 'f',
        'ף': 'f',
        'צ': 'tz',
        'ץ': 'tz',
        'ק': 'k',
        'ר': 'r',
        'ש': 'sh',
        'ת': 't',
        'ַ': 'a',
        'ָ': 'a',
        'ֶ': 'e',
        'ֵ': 'e',
        'ִ': 'i',
        'ֹ': 'o',
        'ֻ': 'u',
        'ֱ': 'e',
        'ֲ': 'a',
        'ֳ': 'o',
        '־': '-',
        ' ': ' ',
    }

    exceptions = {
        'בּ': 'בּ',
        'בּ': 'b',
        'כּ': 'כּ',
        'כּ': 'k',
        'ךּ': 'k',
        'פּ': 'פּ',
        'פּ': 'p',
        'שׁ': 'שׁ',
        'שׁ': 'sh',
        'שׂ': 'שׂ',
        'שׂ': 's',
        'וּ': 'u',
        'וֹ': 'o',
        'ִי': 'i',
        'ּ': '',
        'ְ': '',
        'ׁ': '',
    }

    text = language.smart_shva(text)

    if number_style == 'words':
        def num2word(m):
            return num2words(int(m.group()), lang='he')
        text = re.sub(r'\b\d+\b', num2word, text)

    for k, v in exceptions.items():
        text = text.replace(k, v)

    stolen_positions = []
    for m in re.finditer(r'([חע])ַ(?=\b)', text):
        stolen_positions.append(m.start())

    translit = ""
    for i, char in enumerate(text):
        translit += hebrew_transliteration.get(char, char)

    for pos in stolen_positions:
        translit = re.sub(r'kha\b', 'akh', translit)

    return translit
