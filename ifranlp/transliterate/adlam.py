def transliterate_adlam(text):
    adlam_transliteration = {
        '𞤀': 'A', '𞤢': 'a',
        '𞤁': 'D', '𞤣': 'd',
        '𞤂': 'L', '𞤤': 'l',
        '𞤃': 'M', '𞤥': 'm',
        '𞤄': 'B', '𞤦': 'b',
        '𞤅': 'S', '𞤧': 's',
        '𞤆': 'P', '𞤨': 'p',
        '𞤇': 'Ɓ', '𞤩': 'ɓ',
        '𞤈': 'R', '𞤪': 'r',
        '𞤉': 'E', '𞤫': 'e',
        '𞤊': 'F', '𞤬': 'f',
        '𞤋': 'I', '𞤭': 'i',
        '𞤌': 'O', '𞤮': 'o',
        '𞤍': 'Ɗ', '𞤯': 'ɗ',
        '𞤎': 'Ƴ', '𞤰': 'ƴ',
        '𞤏': 'W', '𞤱': 'w',
        '𞤐': 'N', '𞤲': 'n',
        '𞤑': 'K', '𞤳': 'k',
        '𞤒': 'Y', '𞤴': 'y',
        '𞤓': 'U', '𞤵': 'u',
        '𞤔': 'J', '𞤶': 'j',
        '𞤕': 'C', '𞤷': 'c',
        '𞤖': 'H', '𞤸': 'h',
        '𞤗': 'Ɠ', '𞤹': 'ɠ',
        '𞤘': 'G', '𞤺': 'g',
        '𞤙': 'Ñ', '𞤻': 'ñ',
        '𞤚': 'T', '𞤼': 't',
        '𞤛': 'Ŋ', '𞤽': 'ŋ',

        '𞤜': 'V', '𞤾': 'v',
        '𞤝': 'X', '𞤿': 'x',
        '𞤞': 'GB', '𞥀': 'gb',
        '𞤟': 'Z', '𞥁': 'z',
        '𞤠': 'KP', '𞥂': 'kp',
        '𞤡': 'SH', '𞥃': 'sh',

        # Punctuation
        '؟': '?',  # Question mark (Tyapo)
        '𞥌': '.',  # Period
        '𞥍': ',',  # Comma
        '𞥎': ';',  # Semicolon
        '𞥏': ':',  # Colon

        '𞥅': '̄', '𞥄': '̄', '𞥆': '', '𞥋': '\'',

        # Numbers
        '𞥐': '0', '𞥑': '1', '𞥒': '2', '𞥓': '3', '𞥔': '4',
        '𞥕': '5', '𞥖': '6', '𞥗': '7', '𞥘': '8', '𞥙': '9'
    }

    transliterated_text = ''
    for char in text:
        transliterated_char = adlam_transliteration.get(char, char)
        transliterated_text += transliterated_char

    return transliterated_text