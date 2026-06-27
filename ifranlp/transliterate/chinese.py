from pypinyin import pinyin, Style
from num2words import num2words
import re

def transliterate_chinese(text, number_style='keep'):
    punctuation = {
        '，': ',',
        '、': ',',
        '。': '.',
        '（': '(',
        '）': ')',
        '？': '?',
        '！': '!'
    }

    manipulation = {
        ' ,': ',',
        ' .': '.',
        ' ?': '?',
        ' !': '!',
        '\n ': '\n'
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='zh-CN')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    if not text:
        return ""

    for exception, replacement in punctuation.items():
        text = text.replace(exception, replacement)

    pinyin_list = pinyin(
        text,
        style=Style.TONE,
        heteronym=True,
    )

    output = " ".join([item[0] for item in pinyin_list])

    for exception, replacement in manipulation.items():
        output = output.replace(exception, replacement)

    return output