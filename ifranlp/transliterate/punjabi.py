def transliterate_punjabi(text):
    punjabi_transliteration = {
        'ਅ': 'a',
        'ਆ': 'ā',
        'ਇ': 'i',
        'ਈ': 'ī',
        'ਉ': 'u',
        'ਊ': 'ū',
        'ਏ': 'e',
        'ਐ': 'ai',
        'ਓ': 'o',
        'ਔ': 'au',
        'ਕ': 'k',
        'ਖ': 'kh',
        'ਗ': 'g',
        'ਘ': 'gh',
        'ਙ': 'ng',  # Gurmukhi nasal
        'ਚ': 'ch',
        'ਛ': 'chh',
        'ਜ': 'j',
        'ਝ': 'jh',
        'ਟ': 'ṭ',  # Retroflex
        'ਠ': 'ṭh',  # Retroflex
        'ਡ': 'ḍ',  # Retroflex
        'ਢ': 'ḍh',  # Retroflex
        'ਤ': 't',
        'ਥ': 'th',
        'ਦ': 'd',
        'ਧ': 'dh',
        'ਪ': 'p',
        'ਫ': 'ph',
        'ਬ': 'b',
        'ਭ': 'bh',
        'ਮ': 'm',
        'ਨ': 'n',
        'ਣ': 'ṇ',  # Retroflex nasal
        'ਯ': 'y',
        'ਰ': 'r',
        'ਲ': 'l',
        'ਵ': 'v',
        'ਸ਼': 'sh',
        'ਸ': 's',
        'ਹ': 'h',
        'ਾ': 'ā',
        '੍': '',  # Virama (Halant)
        'ਿ': 'i',
        'ੀ': 'ī',
        'ੁ': 'u',
        'ੂ': 'ū',
        'ੇ': 'ē',
        'ੈ': 'ai',
        'ੋ': 'o',
        'ੌ': 'au',
        'ੰ': 'n',  # Anusvara
        'ਂ': 'ṁ',
        # Skip 'ੱ' and 'ਾ'
        '੦': '0',
        '੧': '1',
        '੨': '2',
        '੩': '3',
        '੪': '4',
        '੫': '5',
        '੬': '6',
        '੭': '7',
        '੮': '8',
        '੯': '9',
        '।': '.',
        # More mappings if needed
    }

    vowels = ('ਅ', 'ਆ', 'ਇ', 'ਈ', 'ਉ', 'ਊ', 'ਏ', 'ਐ', 'ਓ', 'ਔ', 'ਿ', 'ੀ', 'ੁ', 'ੂ', 'ੇ', 'ੈ', 'ੋ', 'ੌ', 'ਾ',)

    transliterated_text = ''
    prev_char = ''
    capitalize_next = True

    for i, char in enumerate(text):
        if char in ('ੱ', '੍', '਼'):
            continue

        elif char in punjabi_transliteration:
            if char in vowels:
                transliterated_text += punjabi_transliteration[char]
            else:
                # Avoid unnecessary 'a' insertion
                if i > 0 and text[i - 1] in punjabi_transliteration and text[i - 1] not in vowels and char not in vowels:
                    transliterated_text += 'a' + punjabi_transliteration[char]
                else:
                    transliterated_text += punjabi_transliteration[char]

        else:
            transliterated_text += char

    return transliterated_text
