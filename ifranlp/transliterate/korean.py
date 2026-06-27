import unicodedata
from num2words import num2words
import re

def transliterate_korean(text, number_style='keep'):
    transliteration_map = {
        'ᄀ': 'g', 'ᄁ': 'kk', 'ᄂ': 'n', 'ᄃ': 'd', 'ᄄ': 'tt', 'ᄅ': 'l', 'ᄆ': 'm',
        'ᄇ': 'b', 'ᄈ': 'pp', 'ᄉ': 's', 'ᄊ': 'ss', 'ᄋ': '', 'ᄌ': 'j', 'ᄍ': 'jj',
        'ᄎ': 'ch', 'ᄏ': 'k', 'ᄐ': 't', 'ᄑ': 'p', 'ᄒ': 'h',
        'ᅡ': 'a', 'ᅢ': 'ae', 'ᅣ': 'ya', 'ᅤ': 'yae', 'ᅥ': 'eo', 'ᅦ': 'e', 'ᅧ': 'yeo',
        'ᅨ': 'ye', 'ᅩ': 'o', 'ᅪ': 'wa', 'ᅫ': 'wae', 'ᅬ': 'oe', 'ᅭ': 'yo', 'ᅮ': 'u',
        'ᅯ': 'wo', 'ᅰ': 'we', 'ᅱ': 'wi', 'ᅲ': 'yu', 'ᅳ': 'eu', 'ᅴ': 'ui', 'ᅵ': 'i',
        'ᆨ': 'k', 'ᆩ': 'kk', 'ᆫ': 'n', 'ᆮ': 't', 'ᆯ': 'l', 'ᆷ': 'm', 'ᆸ': 'p', 'ᆺ': 't',
        'ᆻ': 't', 'ᆼ': 'ng', 'ᆽ': 't', 'ᆾ': 't', 'ᆿ': 'k', 'ᇀ': 't', 'ᇁ': 'p', 'ᇂ': 't',

        'ᆪ': 'ks', 'ᆬ': 'nj', 'ᆭ': 'nh', 'ᆰ': 'lg', 'ᆱ': 'lm', 'ᆲ': 'lb', 'ᆳ': 'ls',
        'ᆴ': 'lt', 'ᆵ': 'lp', 'ᆶ': 'lh', 'ᆹ': 'bs'
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='ko')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        if '가' <= char <= '힣':
            decomposed = unicodedata.normalize('NFD', char)
            for jamo in decomposed:
                transliterated_text += transliteration_map.get(jamo, jamo)
        else:
            transliterated_text += char

    return transliterated_text