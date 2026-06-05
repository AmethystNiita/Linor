from num2words import num2words
import re

def pronunciate_german(text, style='standard', number_style='keep'):
    # longer patterns first so shorter ones don't mess them up
    if style == "casual":
        german_exceptions = [
            # whole-word prefixes / exceptions
            (r'\bVer', 'Fair'),
            (r'\bver', 'fair'),
            (r'\bWer', 'Vair'),
            (r'\bwer', 'vair'),
            (r'\bDer\b', 'Dair'),
            (r'\bder\b', 'dair'),
            (r'\bHer', 'Hair'),
            (r'\bher', 'hair'),

            # common endings
            (r'ieren\b', 'eeren'),
            (r'ehen\b', 'eyn'),
            (r'ehn\b', 'ayn'),
            (r'ehr\b', 'air'),
            (r'eln\b', 'eln'),
            (r'chen\b', 'khen'),
            (r'lich\b', 'likh'),
            (r'ig\b', 'ikh'),
            (r'ich\b', 'ikh'),
            (r'er\b', 'uh'),

            # vowels
            (r'ei', 'eye'),
            (r'ie', 'ee'),
            (r'ir', 'eer'),
            (r'eu', 'oy'),
            (r'äu', 'oy'),
            (r'ä', 'eh'),
            (r'eh', 'ay'),
            (r'är', 'ea'),
            (r'\bÄr', 'Ea'),

            # ch after vowels
            (r'ach', 'akh'),
            (r'och', 'okh'),
            (r'uch', 'ukh'),

            # consonant swaps
            (r'sch', 'sh'),
            (r'Sch', 'Sh'),
            (r'ch', 'kh'),
            (r'\bst', 'sht'),
            (r'\bisht', 'ist'),  # prevent weird over-replace
            (r'v', 'f'),
            (r'V', 'F'),
            (r'w', 'v'),
            (r'W', 'V'),
            (r'ph', 'f'),
            (r'z', 'ts'),
            (r'Z', 'Ts'),
            (r'j', 'y'),
            (r'J', 'Y'),
            (r'ö', 'er'),
            (r'ü', 'oo'),
            (r'Ä', 'Eh'),
            (r'Ö', 'er'),
            (r'Ü', 'U'),

            # ß
            (r'ß', 'ss'),
        ]
    else:
        german_exceptions = [
            # whole-word replacements
            (r'\bVer', 'Feā'),
            (r'\bver', 'feā'),
            (r'\bWer', 'Veā'),
            (r'\bwer', 'veā'),
            (r'\bDer\b', 'Deā'),
            (r'\bder\b', 'deā'),
            (r'\bHer', 'Heā'),
            (r'\bher', 'heā'),

            # suffixes and endings
            (r'ieren\b', 'īarən'),
            (r'ehen\b', 'ēn'),
            (r'ehn\b', 'ēn'),
            (r'ehr\b', 'eā'),
            (r'eln\b', 'əln'),
            (r'chen\b', 'çen'),
            (r'lich\b', 'liç'),
            (r'ig\b', 'iç'),
            (r'ich\b', 'iç'),
            (r'euch', 'ɔiç'),
            (r'er\b', 'ā'),
            (r'är', 'æā'),
            (r'\bÄr', 'Æā'),

            # vowels
            (r'ei', 'ai'),
            (r'ie', 'ī'),
            (r'ir', 'iā'),
            (r'eu', 'ɔi'),
            (r'äu', 'ɔi'),
            (r'ä', 'ē'),
            (r'eh', 'ē'),

            # ch + vowels
            (r'ach', 'aḥ'),
            (r'och', 'ɔḥ'),
            (r'uch', 'uḥ'),

            # consonant swaps
            (r'ch', 'ç'),
            (r'sch', 'š'),
            (r'Sch', 'Š'),
            (r'st', 'št'),
            (r'\bišt', 'ist'),  # fix over-replacement
            (r'v', 'f'),
            (r'V', 'F'),
            (r'w', 'v'),
            (r'W', 'V'),
            (r'ph', 'f'),
            (r'z', 'ts'),
            (r'Z', 'Ts'),
            (r'j', 'y'),
            (r'J', 'Y'),
            (r'ö', 'ø'),
            (r'Ä', 'Ē'),
            (r'Ö', 'Ø'),

            # ß
            (r'ß', 'ss'),
        ]

    def number_to_german_words(match):
        number = int(match.group())
        return num2words(number, lang='de')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_german_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    # apply replacements in order
    for pattern, repl in german_exceptions:
        text = re.sub(pattern, repl, text)

    return text
