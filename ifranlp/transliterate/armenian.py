import re
from num2words import num2words

def transliterate_armenian(text, number_style='keep'):
    chars = {
        "ու": "u", "Ու": "U",
        "Ա": "A", "Բ": "B", "Գ": "G", "Դ": "D", "Ե": "Ye", "Զ": "Z", "Է": "E", "Ը": "Ə", "Թ": "Tʿ",
        "Ժ": "Zh", "Ի": "I", "Լ": "L", "Խ": "Kh", "Ծ": "Ts", "Կ": "K", "Հ": "H", "Ձ": "Dz",
        "Ղ": "Gh", "Ճ": "Tch", "Մ": "M", "Յ": "Y", "Ն": "N", "Շ": "Sh", "Ո": "Vo", "Չ": "Ch",
        "Պ": "P", "Ջ": "J", "Ռ": "Ṙ", "Ս": "S", "Վ": "V", "Տ": "T", "Ր": "R", "Ց": "Tsʿ",
        "Ւ": "W", "Փ": "Pʿ", "Ք": "Kʿ", "Օ": "O", "Ֆ": "F",
        "ա": "a", "բ": "b", "գ": "g", "դ": "d", "ե": "ye", "զ": "z", "է": "e", "ը": "ə", "թ": "tʿ",
        "ժ": "zh", "ի": "i", "լ": "l", "խ": "kh", "ծ": "ts", "կ": "k", "հ": "h", "ձ": "dz",
        "ղ": "gh", "ճ": "tch", "մ": "m", "յ": "y", "ն": "n", "շ": "sh", "ո": "vo", "չ": "ch",
        "պ": "p", "ջ": "j", "ռ": "ṙ", "ս": "s", "վ": "v", "տ": "t", "ր": "r", "ց": "tsʿ",
        "ւ": "w", "փ": "pʿ", "ք": "kʿ", "օ": "o", "ֆ": "f", "և": "yev", "՞": "", "՚": "", "։": '.'
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='hy')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    result = ""
    for char in text:
        result += chars.get(char, char)
    return result
