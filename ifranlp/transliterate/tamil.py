def transliterate_tamil(text, style='standard'):
    transliteration_map = {}

    if style == 'formal':
        transliteration_map = {
            'அ': 'a', 'ஆ': 'ā', 'இ': 'i', 'ஈ': 'ī', 'உ': 'u', 'ஊ': 'ū',
            'எ': 'e', 'ஏ': 'ē', 'ஐ': 'ai', 'ஒ': 'o', 'ஓ': 'ō', 'ஔ': 'au',
            'க': 'k', 'ங': 'ṅ', 'ச': 'c', 'ஜ': 'j', 'ஞ': 'ñ', 'ட': 'ṭ',
            'ண': 'ṇ', 'த': 't', 'ந': 'n', 'ப': 'p', 'ம': 'm', 'ய': 'y',
            'ர': 'r', 'ல': 'l', 'வ': 'v', 'ழ': 'ḻ', 'ள': 'ḷ', 'ற': 'ṟ',
            'ன': 'ṉ', 'ஶ': 'ś', 'ஷ': 'ṣ', 'ஸ': 's', 'ஹ': 'h', 'க்ஷ': 'kṣ',
            'ா': 'ā', 'ி': 'i', 'ீ': 'ī', 'ு': 'u', 'ூ': 'ū',
            'ெ': 'e', 'ே': 'ē', 'ை': 'ai', 'ொ': 'o', 'ோ': 'ō', 'ௌ': 'au',
            '்': '', ' ': ' ', '.': '.', ',': ',',
        }
    elif style == 'casual':
        transliteration_map = {
            'அ': 'a', 'ஆ': 'a', 'இ': 'i', 'ஈ': 'i', 'உ': 'u', 'ஊ': 'u',
            'எ': 'e', 'ஏ': 'e', 'ஐ': 'ai', 'ஒ': 'o', 'ஓ': 'o', 'ஔ': 'ou',
            'க': 'k', 'ங': 'ng', 'ச': 'c', 'ஜ': 'j', 'ஞ': 'nj', 'ட': 't',
            'ண': 'n', 'த': 'th', 'ந': 'n', 'ப': 'p', 'ம': 'm', 'ய': 'y',
            'ர': 'r', 'ல': 'l', 'வ': 'v', 'ழ': 'zh', 'ள': 'l', 'ற': 'r',
            'ன': 'n', 'ஶ': 'sh', 'ஷ': 'sh', 'ஸ': 's', 'ஹ': 'h', 'க்ஷ': 'ksh',
            'ா': 'a', 'ி': 'i', 'ீ': 'i', 'ு': 'u', 'ூ': 'oo',
            'ெ': 'e', 'ே': 'e', 'ை': 'ai', 'ொ': 'o', 'ோ': 'o', 'ௌ': 'ou',
            '்': '', ' ': ' ', '.': '.', ',': ',',
        }
    else:  # 'standard' is the default
        transliteration_map = {
            'அ': 'a', 'ஆ': 'aa', 'இ': 'i', 'ஈ': 'ee', 'உ': 'u', 'ஊ': 'oo',
            'எ': 'e', 'ஏ': 'e', 'ஐ': 'ai', 'ஒ': 'o', 'ஓ': 'o', 'ஔ': 'au',
            'க': 'k', 'ங': 'ng', 'ச': 'c', 'ஜ': 'j', 'ஞ': 'nj', 'ட': 't',
            'ண': 'n', 'த': 'th', 'ந': 'n', 'ப': 'p', 'ம': 'm', 'ய': 'y',
            'ர': 'r', 'ல': 'l', 'வ': 'v', 'ழ': 'zh', 'ள': 'l', 'ற': 'r',
            'ன': 'n', 'ஶ': 'sh', 'ஷ': 'sh', 'ஸ': 's', 'ஹ': 'h', 'க்ஷ': 'ksh',
            'ா': 'aa', 'ி': 'i', 'ீ': 'ee', 'ு': 'u', 'ூ': 'oo',
            'ெ': 'e', 'ே': 'e', 'ை': 'ai', 'ொ': 'o', 'ோ': 'o', 'ௌ': 'ou',
            '்': '', ' ': ' ', '.': '.', ',': ',',
        }

    # Your existing logic to handle Tamil script structure
    result = ""
    i = 0
    while i < len(text):
        char = text[i]

        if i + 1 < len(text) and (text[i] + text[i + 1]) in transliteration_map:
            result += transliteration_map[text[i] + text[i + 1]]
            i += 2
            continue

        if char in 'கஙசஜஞடணதநபமயரலவழளறனஶஷஸஹ' and i + 1 < len(text) and text[i + 1] == '்':
            result += transliteration_map[char]
            i += 2
            continue

        if char in 'கஙசஜஞடணதநபமயரலவழளறனஶஷஸஹ' and i + 1 < len(text) and text[i + 1] in 'ாிீுூெேைொோௌ':
            base_consonant = transliteration_map[char]
            vowel_sign = transliteration_map[text[i + 1]]
            result += base_consonant + vowel_sign
            i += 2
            continue

        if char in transliteration_map:
            if char in 'கஙசஜஞடணதநபமயரலவழளறனஶஷஸஹ':
                result += transliteration_map[char] + 'a'
            else:
                result += transliteration_map[char]
        else:
            result += char

        i += 1

    return result