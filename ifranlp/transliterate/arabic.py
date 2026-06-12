from num2words import num2words
from ifranlp.diacritize import arabic
import re

def transliterate_arabic(text, style='standard', number_style='keep', assimilation_style='off', prefix_style='off'):
    if style == 'formal':
        arabic_transliteration = {
            'ا': 'ā', 'ب': 'b', 'ت': 't', 'ث': 'ṯ', 'ج': 'j', 'ح': 'ħ', 'خ': 'ḵ',
            'د': 'd', 'ذ': 'ḏ', 'ر': 'r', 'ز': 'z', 'س': 's', 'ش': 'š', 'ص': 'ṣ', 'ض': 'ḍ',
            'ط': 'ṭ', 'ظ': 'ẓ', 'ع': 'ʿ', 'غ': 'ġ', 'ف': 'f', 'ق': 'q', 'ك': 'k', 'ل': 'l',
            'م': 'm', 'ن': 'n', 'ه': 'h', 'و': 'w', 'ي': 'y', 'ء': 'ʾ', 'أ': 'ʾ', 'إ': 'ʾi',
            'ؤ': 'ʾ', 'ئ': 'ʾ', 'ى': 'ā', 'ة': 'h', 'آ': 'ʾā',
            'َ': 'a', 'ِ': 'i', 'ُ': 'u', 'ً': 'an', 'ٍ': 'in', 'ٌ': 'un',
            'ْ': '', 'ٰ': 'ā', '؟': '?', '،': ',',
            '١': '1', '٢': '2', '٣': '3', '٤': '4', '۴': '4', '٥': '5', '۵': '5',
            '٦': '6', '۶': '6', '٧': '7', '٨': '8', '٩': '9', '٠': '0',
        }

    elif style == 'casual':
        arabic_transliteration = {
            'ا': 'a', 'ب': 'b', 'ت': 't', 'ث': 'th', 'ج': 'j', 'ح': '7', 'خ': '5',
            'د': 'd', 'ذ': '4', 'ر': 'r', 'ز': 'z', 'س': 's', 'ش': 'sh', 'ص': '9', 'ض': '9\'',
            'ط': '6', 'ظ': 'z', 'ع': '3', 'غ': '3\'', 'ف': 'f', 'ق': 'q', 'ك': 'k', 'ل': 'l',
            'م': 'm', 'ن': 'n', 'ه': 'h', 'و': 'w', 'ي': 'y', 'ء': '2', 'أ': '2', 'إ': '2i',
            'ؤ': '2', 'ئ': '2', 'ى': 'a', 'ة': 'h', 'آ': '2a',
            'َ': 'a', 'ِ': 'i', 'ُ': 'u', 'ً': 'an', 'ٍ': 'in', 'ٌ': 'un',
            'ْ': '', 'ّ': '', 'ٰ': 'a', '؟': '?', '،': ',',
            '١': '1', '٢': '2', '٣': '3', '٤': '4', '۴': '4', '٥': '5', '۵': '5',
            '٦': '6', '۶': '6', '٧': '7', '٨': '8', '٩': '9', '٠': '0',
        }

    elif style == 'ascii':
        arabic_transliteration = {
            'ا': 'a', 'ب': 'b', 'ت': 't', 'ث': 'th', 'ج': 'j', 'ح': 'H', 'خ': 'K',
            'د': 'd', 'ذ': 'dh', 'ر': 'r', 'ز': 'z', 'س': 's', 'ش': 'sh', 'ص': 'S', 'ض': 'D',
            'ط': 'T', 'ظ': 'Z', 'ع': 'E', 'غ': 'gh', 'ف': 'f', 'ق': 'q', 'ك': 'k', 'ل': 'l',
            'م': 'm', 'ن': 'n', 'ه': 'h', 'و': 'w', 'ي': 'y', 'ء': '2', 'أ': '2', 'إ': '2i',
            'ؤ': '2', 'ئ': '2', 'ى': 'a', 'ة': 'h', 'آ': '2a',
            'َ': 'a', 'ِ': 'i', 'ُ': 'u', 'ً': 'an', 'ٍ': 'in', 'ٌ': 'un',
            'ْ': '', 'ّ': '', 'ٰ': 'a', '؟': '?', '،': ',',
            '١': '1', '٢': '2', '٣': '3', '٤': '4', '۴': '4', '٥': '5', '۵': '5',
            '٦': '6', '۶': '6', '٧': '7', '٨': '8', '٩': '9', '٠': '0',
        }

    else:
        arabic_transliteration = {
            'ا': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 'th', 'ج': 'j', 'ح': 'h', 'خ': 'kh',
            'د': 'd', 'ذ': 'dh', 'ر': 'r', 'ز': 'z', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'd',
            'ط': 't', 'ظ': 'z', 'ع': 'e', 'غ': 'gh', 'ف': 'f', 'ق': 'q', 'ك': 'k', 'ل': 'l',
            'م': 'm', 'ن': 'n', 'ه': 'h', 'و': 'w', 'ي': 'y', 'ء': '\'', 'أ': '\'', 'إ': '\'i',
            'ؤ': '\'', 'ئ': '\'', 'ى': 'a', 'ة': 'h', 'آ': '\'a',
            'َ': 'a', 'ٱ': 'a', 'ِ': 'i', 'ُ': 'u', 'ً': 'an', 'ٍ': 'in', 'ٌ': 'un',
            'ْ': '', 'ّ': '', 'ٰ': 'a', '؟': '?', '،': ',',
            '١': '1', '٢': '2', '٣': '3', '٤': '4', '۴': '4', '٥': '5', '۵': '5',
            '٦': '6', '۶': '6', '٧': '7', '٨': '8', '٩': '9', '٠': '0',
        }

    tanwiin = ['ً', 'ٍ', 'ٌ', 'ْ']

    if prefix_style == "on":
        prefixes = {
            ' وَبِ': ' wa-bi-',
            ' وَلِ': ' wa-li-',
            ' وَكَ': ' wa-ka-',

            ' فَبِ': ' fa-bi-',
            ' فَلِ': ' fa-li-',
            ' فَكَ': ' fa-ka-',

            ' وَسَ': ' wa-sa-',
            ' فَسَ': ' fa-sa-',

            ' بِ': ' bi-',
            ' لِ': ' li-',
            ' كَ': ' ka-',
            ' وَ': ' wa-',
            ' فَ': ' fa-',
            ' سَ': ' sa-'
        }
    else:
        prefixes = {}

    if assimilation_style == "on":
        fourth_exceptions = {
            'التّ': 'ت-ت', 'الثّ': 'ث-ث', 'الدّ': 'د-د', 'الذّ': 'ذ-ذ',
            'الرّ': 'ر-ر', 'الزّ': 'ز-ز', 'السّ': 'س-س', 'الشّ': 'ش-ش',
            'الصّ': 'ص-ص', 'الضّ': 'ض-ض', 'الطّ': 'ط-ط', 'الظّ': 'ظ-ظ',
            'اللّ': 'ل-ل', 'النّ': 'ن-ن',
            'الْب': 'ل-ب', 'الْج': 'ل-ج', 'الْح': 'ل-ح', 'الْخ': 'ل-خ',
            'الْع': 'ل-ع', 'الْغ': 'ل-غ', 'الْف': 'ل-ف', 'الْق': 'ل-ق',
            'الْك': 'ل-ك', 'الْم': 'ل-م', 'الْه': 'ل-ه', 'الْو': 'ل-و',
            'الْي': 'ل-ي', 'الْء': 'ل-ء',
        }
    else:
        fourth_exceptions = {}

    exceptions = {
        'أَ': 'ءَ', 'إِ': 'ءِ', 'أُ': 'ءُ',
        'ئَ': 'ءَ', 'ئِ': 'ءِ', 'ئُ': 'ءُ',
        'الله': 'اللاه',
        'ةَ': 'تَ', 'ةِ': 'تِ', 'ةُ': 'تُ',
        'ةً': 'تً', 'ةٍ': 'تٍ', 'ةٌ': 'تٌ',
    }

    first_exceptions = {
        'َّ': 'َّ', 'ِّ': 'ِّ', 'ُّ': 'ُّ',
        'ًّ': 'ًّ', 'ٍّ': 'ٍّ', 'ٌّ': 'ٌّ',
        'ّْ': 'ّْ', 'ًا': 'ً', 'اً': 'ً',
        'اِ': 'ِ', 'ُوا': 'ُو'
    }

    second_exceptions = {
        'ُوَ': 'uwa', 'ُوِ': 'uwi', 'ُوُ': 'uwu',
        'ُوَّ': 'uwwa', 'ُوِّ': 'uwwi', 'ُوُّ': 'uwwu',
        'ِيَ': 'iya', 'ِيِ': 'iyi', 'ِيُ': 'iyu',
        'ِيَّ': 'iyya', 'ِيِّ': 'iyyi', 'ِيُّ': 'iyyu',
        'ُوً': 'uwan', 'ُوٍ': 'uwin', 'ُوٌ': 'uwun',
        'ُوًّ': 'uwwan', 'ُوٍّ': 'uwwin', 'ُوٌّ': 'uwwun',
        'ِيً': 'iyan', 'ِيٍ': 'iyin', 'ِيٌ': 'iyun',
        'ِيًّ': 'iyyan', 'ِيٍّ': 'iyyin', 'ِيٌّ': 'iyyun',
        'aا': 'ا', 'iي': 'ِي', 'uو': 'ُو',
        'anا': 'an'
    }

    if style == 'formal':
        third_exceptions = {
            'ُو': 'ū', 'ِي': 'ī', 'وْ': 'w',
            'َى': 'ى', 'ِى': 'ī', 'َٰ': 'ا'
        }
    else:
        third_exceptions = {
            'ُو': 'ُ', 'ِي': 'ِ', 'وْ': 'w',
            'َى': 'ى', 'ِى': 'ِي', 'َٰ': 'ا'
        }

    def number_to_arabic_words(match):
        number = int(match.group())
        return num2words(number, lang='ar')

    def replace_numbers_with_words(text):
        return re.sub(r'\b\d+\b', number_to_arabic_words, text)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    text = arabic.diacritize(text)

    for exception, replacement in exceptions.items():
        text = text.replace(exception, replacement)

    for exception, replacement in first_exceptions.items():
        text = text.replace(exception, replacement)

    for exception, replacement in second_exceptions.items():
        text = text.replace(exception, replacement)

    for exception, replacement in third_exceptions.items():
        text = text.replace(exception, replacement)

    for exception, replacement in fourth_exceptions.items():
        for char in tanwiin:
            if f"{char} {exception}" in text:
                text = text.replace(f"{char} {exception}", f"{char} a{exception}")
            elif f"، {exception}" in text:
                text = text.replace(f"، {exception}", f"، a{exception}")
            elif f". {exception}" in text:
                text = text.replace(f". {exception}", f". a{exception}")
            elif f"؟ {exception}" in text:
                text = text.replace(f"؟ {exception}", f"؟ a{exception}")
            elif f"\n{exception}" in text:
                text = text.replace(f"\n{exception}", f"\na{exception}")
            elif f"- {exception}" in text:
                text = text.replace(f"- {exception}", f"- a{exception}")
            elif text.startswith(exception):
                text = f"a{replacement}" + text[len(exception):]

        if exception in text:
            text = text.replace(exception, replacement)

    for exception, replacement in prefixes.items():
        if text.startswith(exception[1:]):
            text = f"{replacement[1:]}" + text[len(exception[1:]):]
        elif exception in text:
            text = text.replace(exception, replacement)

    text = text.replace('َا', 'ا')

    transliterated_text = ''
    i = 0

    while i < len(text):
        char = text[i]

        if char == 'ّ':
            if i > 0:
                prev_char = text[i - 1]
                translit = arabic_transliteration.get(prev_char, prev_char)
                transliterated_text += translit  # Double the previous letter

            i += 1
            continue

        translit = arabic_transliteration.get(char, char)
        transliterated_text += translit

        i += 1

    return transliterated_text