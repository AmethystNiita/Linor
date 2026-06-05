def transliterate_nko(text):
    nko_transliteration = {
        # Vowels
        'ߊ': 'a', 'ߋ': 'e', 'ߌ': 'i', 'ߍ': 'ɛ', 'ߎ': 'u', 'ߏ': 'o', 'ߐ': 'ɔ',

        # Consonants
        'ߓ': 'b', 'ߔ': 'p', 'ߕ': 't', 'ߖ': 'g', 'ߗ': 'č', 'ߘ': 'd', 'ߙ': 'r',
        'ߚ': 'rr', 'ߛ': 's', 'ߜ': 'gb', 'ߝ': 'f', 'ߞ': 'k', 'ߟ': 'l', 'ߠ': 'n',
        'ߡ': 'm', 'ߢ': 'ɲ', 'ߣ': 'n', 'ߤ': 'h', 'ߥ': 'w', 'ߦ': 'j', 'ߒ': 'ŋ', 'ߧ': 'y',

        # Tones and diacritics
        '߫': '',  # High tone
        '߬': '',  # Low tonk
        '߭': '',  # Ascending tone

        '߮': '̄',  # High long tone
        '߯': '̄',  # Low long tone
        '߰': '̄',
        '߱': '̄',
        '߲': 'n',


        '،': ',',
        '߸': ',',
        '߹': '!',

        # Numbers
        '߀': '0', '߁': '1', '߂': '2', '߃': '3', '߄': '4',
        '߅': '5', '߆': '6', '߇': '7', '߈': '8', '߉': '9'
    }

    transliterated_text = ''
    for char in text:
        transliterated_char = nko_transliteration.get(char, char)
        transliterated_text += transliterated_char

    return transliterated_text