from num2words import num2words
import re

def transliterate_russian(text, number_style='keep'):
    russian_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'ḥ',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': '\"',
        'ы': 'y',
        'ь': '\'',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    def number_to_russian_words(match):
        number = int(match.group())
        return num2words(number, lang='ru')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_russian_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        transliterated_char = russian_transliteration.get(char.lower(), char)
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_ukrainian(text, number_style='keep'):
    ukrainian_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'h',
        'ґ': 'g',
        'д': 'd',
        'е': 'e',
        'є': 'ye',
        'ж': 'zh',
        'з': 'z',
        'и': 'y',
        'і': 'i',
        'ї': 'yi',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'ḥ',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ь': '\'',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='uk')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        # Use the transliteration mapping, or keep the original character if not found
        transliterated_char = ukrainian_transliteration.get(char.lower(), char)
        # Preserve the case (upper or lower) of the original character
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_serbian(text, number_style='keep'):
    serbian_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'ђ': 'đ',
        'е': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'ј': 'y',
        'к': 'k',
        'л': 'l',
        'љ': 'ly',
        'м': 'm',
        'н': 'n',
        'њ': 'ny',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'ћ': 'ć',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'џ': 'dzh',
        'ш': 'sh',
        # Add more mappings as needed
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='sr')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        # Use the transliteration mapping, or keep the original character if not found
        transliterated_char = serbian_transliteration.get(char.lower(), char)
        # Preserve the case (upper or lower) of the original character
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_belarusian(text, number_style='keep'):
    belarusian_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'h',
        'ґ': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'і': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ў': 'u',
        'ф': 'f',
        'х': 'ḥ',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'ь': '\'',
        'ы': 'y',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='by')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        # Use the transliteration mapping, or keep the original character if not found
        transliterated_char = belarusian_transliteration.get(char.lower(), char)
        # Preserve the case (upper or lower) of the original character
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_bulgarian(text):
    bulgarian_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'ḥ',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sht',
        'ъ': 'ŭ',
        'ь': 'ʹ',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    transliterated_text = ''
    for char in text:
        # Use the transliteration mapping, or keep the original character if not found
        transliterated_char = bulgarian_transliteration.get(char.lower(), char)
        # Preserve the case (upper or lower) of the original character
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_macedonian(text):
    macedonian_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'ѓ': 'ǵ',
        'е': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'ј': 'j',
        'к': 'k',
        'л': 'l',
        'љ': 'ly',
        'м': 'm',
        'н': 'n',
        'њ': 'ny',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'ќ': 'ḱ',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'ch',
        'џ': 'ǯ',
        'ш': 'sh'
        # Add more mappings as needed
    }

    transliterated_text = ''
    for char in text:
        # Use the transliteration mapping, or keep the original character if not found
        transliterated_char = macedonian_transliteration.get(char.lower(), char)
        # Preserve the case (upper or lower) of the original character
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_kazakh(text, number_style='keep'):
    kazakh_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'ғ': 'ǵ',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'қ': 'q',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'ң': 'ń',
        'о': 'o',
        'ө': 'ö',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'w',
        'ұ': 'u',
        'ү': 'ü',
        'ф': 'f',
        'х': 'x',
        'һ': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': '\"',
        'ы': 'y',
        'і': 'i',
        'ь': '\'',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='kz')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        transliterated_char = kazakh_transliteration.get(char.lower(), char)
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_kyrgyz(text):
    kyrgyz_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'ө': 'ö',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ү': 'ü',
        'ф': 'f',
        'х': 'ḥ',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': '\"',
        'ы': 'y',
        'ь': '\'',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    transliterated_text = ''
    for char in text:
        transliterated_char = kyrgyz_transliteration.get(char.lower(), char)
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_tajik(text, number_style='keep'):
    tajik_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'ғ': 'ǵ',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'ӣ': 'ī',
        'й': 'y',
        'к': 'k',
        'қ': 'q',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ӯ': 'ū',
        'ф': 'f',
        'х': 'kh',
        'ҳ': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ҷ': 'chh',
        'ш': 'sh',
        'ъ': '\"',
        'ы': 'y',
        'ь': '\'',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='tg')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        transliterated_char = tajik_transliteration.get(char.lower(), char)
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text

def transliterate_mongolian(text, number_style='keep'):
    mongolian_transliteration = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'ye',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'ө': 'ö',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ү': 'ü',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': '\"',
        'ы': 'y',
        'ь': '\'',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
        # Add more mappings as needed
    }

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='mn')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    transliterated_text = ''
    for char in text:
        transliterated_char = mongolian_transliteration.get(char.lower(), char)
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    return transliterated_text


def transliterate_buryat(text):
    mapping = {
        "һ": "h", "Һ": "H",
        "ө": "o", "Ө": "O",
        "ү": "u", "Ү": "U",

        "я": "ya", "Я": "YA",
        "ю": "yu", "Ю": "YU",
        "е": "e", "Е": "E",
        "ё": "yo", "Ё": "YO",

        "ь": "", "Ь": "",
        "ъ": "", "Ъ": "",

        "а": "a", "А": "A",
        "б": "b", "Б": "B",
        "в": "v", "В": "V",
        "г": "g", "Г": "G",
        "д": "d", "Д": "D",
        "ж": "zh", "Ж": "ZH",
        "з": "z", "З": "Z",
        "и": "i", "И": "I",
        "й": "y", "Й": "Y",
        "к": "k", "К": "K",
        "л": "l", "Л": "L",
        "м": "m", "М": "M",
        "н": "n", "Н": "N",
        "п": "p", "П": "P",
        "р": "r", "Р": "R",
        "с": "s", "С": "S",
        "т": "t", "Т": "T",
        "у": "u", "У": "U",
        "ф": "f", "Ф": "F",
        "х": "h", "Х": "H",
        "ц": "ts", "Ц": "TS",
        "ч": "ch", "Ч": "CH",
        "ш": "sh", "Ш": "SH",
        "щ": "shch", "Щ": "SHCH",
        "ы": "y", "Ы": "Y",
        "э": "e", "Э": "E"
    }

    transliterated_text = text
    for bucy, latin in mapping.items():
        transliterated_text = transliterated_text.replace(bucy, latin)

    return transliterated_text