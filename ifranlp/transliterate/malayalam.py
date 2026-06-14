import re


# Helper function to transliterate a single word
def _transliterate_malayalam_word(word, transliteration_map, malayalam_consonants, malayalam_vowel_signs):
    # Handle trailing punctuation
    punctuation = set('.,?!:;')
    trailing_punctuation = ''
    if word and word[-1] in punctuation:
        trailing_punctuation = word[-1]
        word = word[:-1]

    result = []
    i = 0
    while i < len(word):
        char = word[i]

        if char in malayalam_consonants and i + 1 < len(word) and word[i + 1] in malayalam_vowel_signs:
            result.append(transliteration_map.get(char, ''))
            result.append(transliteration_map.get(word[i + 1], ''))
            i += 2
            continue

        if char in malayalam_consonants and i + 1 < len(word) and word[i + 1] == '്':
            result.append(transliteration_map.get(char, ''))
            i += 2
            continue

        if char in malayalam_consonants:
            result.append(transliteration_map.get(char, '') + 'a')
            i += 1
            continue

        result.append(transliteration_map.get(char, char))
        i += 1

    final_result = "".join(result)

    if word.endswith('്'):
        final_result += 'u'

    return final_result + trailing_punctuation


def transliterate_malayalam(text, style='standard'):
    if style == 'formal':
        transliteration_map = {
            'അ': 'a', 'ആ': 'ā', 'ഇ': 'i', 'ഈ': 'ī', 'ഉ': 'u', 'ഊ': 'ū',
            'ഋ': 'r̥', 'എ': 'e', 'ഏ': 'ē', 'ഐ': 'ai', 'ഒ': 'o', 'ഓ': 'ō', 'ഔ': 'au',
            'ക': 'k', 'ഖ': 'kh', 'ഗ': 'g', 'ഘ': 'gh', 'ങ': 'ṅ',
            'ച': 'c', 'ഛ': 'ch', 'ജ': 'j', 'ഝ': 'jh', 'ഞ': 'ñ',
            'ട': 'ṭ', 'ഠ': 'ṭh', 'ഡ': 'ḍ', 'ഢ': 'ḍh', 'ണ': 'ṇ',
            'ത': 't', 'ഥ': 'th', 'ദ': 'd', 'ധ': 'dh', 'ന': 'n',
            'പ': 'p', 'ഫ': 'ph', 'ബ': 'b', 'ഭ': 'bh', 'മ': 'm',
            'യ': 'y', 'ര': 'r', 'ല': 'l', 'വ': 'v',
            'ശ': 'ś', 'ഷ': 'ṣ', 'സ': 's', 'ഹ': 'h', 'ള': 'ḷ', 'ഴ': 'ḻ',
            'റ': 'ṟ',
            '്': '', 'ം': 'ṁ', 'ഃ': 'ḥ',
            'ാ': 'ā', 'ി': 'i', 'ീ': 'ī', 'ു': 'u', 'ൂ': 'ū',
            'ൃ': 'r̥', 'െ': 'e', 'േ': 'ē', 'ൈ': 'ai',
            'ൊ': 'o', 'ോ': 'ō', 'ൌ': 'au', 'ൗ': 'au',
            'ൺ': 'ṇ', 'ൻ': 'n', 'ർ': 'r', 'ൽ': 'l', 'ൾ': 'ḷ',
        }

    elif style == 'casual':
        transliteration_map = {
        'അ': 'a', 'ആ': 'a', 'ഇ': 'i', 'ഈ': 'i', 'ഉ': 'u', 'ഊ': 'u',
        'ഋ': 'ru', 'എ': 'e', 'ഏ': 'e', 'ഐ': 'ai', 'ഒ': 'o', 'ഓ': 'o', 'ഔ': 'ou',
        'ക': 'k', 'ഖ': 'kh', 'ഗ': 'g', 'ഘ': 'gh', 'ങ': 'ng',
        'ച': 'ch', 'ഛ': 'ch', 'ജ': 'j', 'ഝ': 'jh', 'ഞ': 'nj',
        'ട': 't', 'ഠ': 'th', 'ഡ': 'd', 'ഢ': 'dh', 'ണ': 'n',
        'ത': 'th', 'ഥ': 'th', 'ദ': 'd', 'ധ': 'dh', 'ന': 'n',
        'പ': 'p', 'ഫ': 'ph', 'ബ': 'b', 'ഭ': 'bh', 'മ': 'm',
        'യ': 'y', 'ര': 'r', 'ല': 'l', 'വ': 'v',
        'ശ': 'sh', 'ഷ': 'sh', 'സ': 's', 'ഹ': 'h', 'ള': 'l', 'ഴ': 'zh',
        'റ': 'r',
        '്': '', 'ം': 'm', 'ഃ': 'am',
        'ാ': 'a', 'ി': 'i', 'ീ': 'i', 'ു': 'u', 'ൂ': 'u',
        'ൃ': 'ru', 'െ': 'e', 'േ': 'e', 'ൈ': 'ai',
        'ൊ': 'o', 'ോ': 'o', 'ൌ': 'ou', 'ൗ': 'ou',
        'ൺ': 'n', 'ൻ': 'n', 'ർ': 'r', 'ൽ': 'l', 'ൾ': 'l',
        }

    else:
        transliteration_map = {
        'അ': 'a', 'ആ': 'aa', 'ഇ': 'i', 'ഈ': 'ee', 'ഉ': 'u', 'ഊ': 'oo',
        'ഋ': 'ru', 'എ': 'e', 'ഏ': 'e', 'ഐ': 'ai', 'ഒ': 'o', 'ഓ': 'o', 'ഔ': 'ou',
        'ക': 'k', 'ഖ': 'kh', 'ഗ': 'g', 'ഘ': 'gh', 'ങ': 'ng',
        'ച': 'ch', 'ഛ': 'chh', 'ജ': 'j', 'ഝ': 'jh', 'ഞ': 'nj',
        'ട': 't', 'ഠ': 'th', 'ഡ': 'd', 'ഢ': 'dh', 'ണ': 'n',
        'ത': 'th', 'ഥ': 'thh', 'ദ': 'd', 'ധ': 'dh', 'ന': 'n',
        'പ': 'p', 'ഫ': 'ph', 'ബ': 'b', 'ഭ': 'bh', 'മ': 'm',
        'യ': 'y', 'ര': 'r', 'ല': 'l', 'വ': 'v',
        'ശ': 'sh', 'ഷ': 'sh', 'സ': 's', 'ഹ': 'h', 'ള': 'l', 'ഴ': 'zh',
        'റ': 'r',
        '്': '', 'ം': 'm', 'ഃ': 'ah',
        'ാ': 'aa', 'ി': 'i', 'ീ': 'ee', 'ു': 'u', 'ൂ': 'oo',
        'ൃ': 'ru', 'െ': 'e', 'േ': 'e', 'ൈ': 'ai',
        'ൊ': 'o', 'ോ': 'o', 'ൌ': 'ou', 'ൗ': 'ou',
        'ൺ': 'n', 'ൻ': 'n', 'ർ': 'r', 'ൽ': 'l', 'ൾ': 'l',
        }

    malayalam_consonants = set('കഖഗഘങചഛജഝഞടഠഡഢണതഥദധനപഫബഭമയരലവശഷസഹളഴറ')
    malayalam_vowel_signs = set('ാിീുൂൃെേൈൊോൌൗ')

    # Use a regex pattern to match all Malayalam characters
    malayalam_chars_pattern = r'[അ-ഹളഴറൺൻർൽൾംഃാിീുൂൃെേൈൊോൌൗ്]'

    # Define a transliteration function to pass to re.sub
    def translit_replacer(match):
        word = match.group(0)
        return _transliterate_malayalam_word(word, transliteration_map, malayalam_consonants, malayalam_vowel_signs)

    # Replace all Malayalam character sequences with their transliterated versions
    return re.sub(malayalam_chars_pattern + '+', translit_replacer, text)