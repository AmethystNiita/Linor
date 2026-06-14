def transliterate_hindi(text):
    hindi_transliteration = {
        'अ': 'a',
        'आ': 'ā',
        'ऑ': 'o',
        'इ': 'i',
        'ई': 'ee',
        'उ': 'u',
        'ऊ': 'oo',
        'ऋ': 'r',
        'ए': 'e',
        'ऐ': 'ai',
        'ओ': 'o',
        'औ': 'au',
        'क': 'k',
        'ख': 'kh',
        'ग': 'g',
        'घ': 'gh',
        'च': 'ch',
        'छ': 'ch',
        'ज': 'j',
        'झ': 'jh',
        'ञ': 'ny',  # Retroflex nasal
        'ट': 'ṭ',   # Retroflex
        'ठ': 'ṭh',  # Retroflex
        'ड': 'ḍ',   # Retroflex
        'ढ': 'ḍh',  # Retroflex
        'त': 't',
        'थ': 'th',
        'द': 'd',
        'ध': 'dh',
        'प': 'p',
        'फ': 'ph',
        'ब': 'b',
        'भ': 'bh',
        'म': 'm',
        'न': 'n',
        'ण': 'n',
        'य': 'y',
        'र': 'r',
        'ल': 'l',
        'व': 'v',
        'श': 'sh',
        'ष': 'sh',
        'स': 's',
        'ह': 'h',
        'ः': 'h',  # Visarga
        'ं': 'n',  # Anusvara
        'ँ': 'n',  # Candrabindu
        'ा': 'a',
        'ि': 'i',
        'ी': 'ee',
        'ु': 'u',
        'ू': 'uu',
        'े': 'e',
        'ै': 'ai',
        'ो': 'o',
        'ॉ': 'o',
        'ौ': 'au',
        '।': '.',
        '्': '',
        '़': '',  # Handling '्' character
        'ृ': 'r',
        'ज़': 'z',  # Handling 'ज़' character
        '०': '0',
        '१': '1',
        '२': '2',
        '३': '3',
        '४': '4',
        '५': '5',
        '६': '6',
        '७': '7',
        '८': '8',
        '९': '9'
    }

    vowels = ('अ', 'आ', 'ऑ', 'औ', 'ई', 'इ', 'उ', 'ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ॉ', 'ौ', '्', 'ँ', 'ं')

    transliterated_text = ''
    prev_char = ''
    capitalize_next = True

    for i, char in enumerate(text):
        if char == '्':
            # Skip '्' character and continue with the next iteration
            continue

        elif char == 'ज' and i < len(text) - 1 and text[i + 1] == '़':
            transliterated_text += hindi_transliteration.get('ज़', 'z')
            i += 1  # Skip the next character ('़')

        elif char == 'ड' and i < len(text) - 1 and text[i + 1] == '़':
            transliterated_text += hindi_transliteration.get('ड़', 'r')
            i += 1  # Skip the next character ('़')

        elif char in hindi_transliteration:
            if char in vowels:
                transliterated_text += hindi_transliteration[char]
            else:
                # Avoid unnecessary 'a' insertion
                if i > 0 and text[i - 1] in hindi_transliteration and text[i - 1] not in vowels and char not in vowels:
                    transliterated_text += 'a' + hindi_transliteration[char]
                else:
                    transliterated_text += hindi_transliteration[char]

        else:
            transliterated_text += char

    return transliterated_text
