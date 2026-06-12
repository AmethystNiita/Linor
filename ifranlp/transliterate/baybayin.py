import re

def fix_d_and_r(text):
    return re.sub(r'([aeiou])d([aeiou])', r'\1r\2', text)

def transliterate_baybayin(text):
    base_map = {
        'ᜀ': 'a', 'ᜁ': 'i', 'ᜂ': 'u',
        'ᜃ': 'ka', 'ᜄ': 'ga', 'ᜅ': 'nga', 'ᜆ': 'ta', 'ᜇ': 'da',
        'ᜈ': 'na', 'ᜉ': 'pa', 'ᜊ': 'ba', 'ᜋ': 'ma', 'ᜌ': 'ya',
        'ᜎ': 'la', 'ᜏ': 'wa', 'ᜐ': 'sa', 'ᜑ': 'ha', 'ᜍ': 'ra'
    }

    punctuation_map = {
        '᜵': ',', '᜶': '.'
    }

    exceptions = {
        ' buu': ' buo',
        ' uud': ' uod',
        
        ' manga ': ' mga ',
        'uu': 'oo',
        'uy ': 'o\'y ',
        'u ': 'o ',
        ' isat isa': ' isa\'t isa'
    }

    result = []

    for char in text:
        if char in base_map:
            result.append(base_map[char])

        elif char in ('ᜒ', 'ᜓ', '᜔', '᜕') and result:
            last_idx = len(result) - 1
            last_syllable = result[last_idx]

            if last_syllable.endswith('a'):
                base_consonant = last_syllable[:-1]
                if char == 'ᜒ':
                    result[last_idx] = base_consonant + 'i'
                elif char == 'ᜓ':
                    result[last_idx] = base_consonant + 'u'
                elif char in ('᜔', '᜕'):
                    result[last_idx] = base_consonant

        elif char in punctuation_map:
            result.append(punctuation_map[char])
        else:
            result.append(char)

    transliterated = "".join(result)

    words = transliterated.split(" ")
    processed_words = []

    for word in words:
        if len(word) > 0 and len(word) % 2 == 0:
            mid = len(word) // 2
            left = word[:mid]
            right = word[mid:]
            if left == right:
                word = f"{left}-{right}"
        processed_words.append(word)

    transliterated = " ".join(processed_words)

    for exception, replacement in exceptions.items():
        transliterated = transliterated.replace(exception, replacement)

    transliterated = fix_d_and_r(transliterated)

    return transliterated