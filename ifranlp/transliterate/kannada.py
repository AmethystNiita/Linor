def transliterate_kannada(text, style='standard'):
    if style == 'formal':
        transliteration_map= {
            'ಅ': 'a', 'ಆ': 'ā', 'ಇ': 'i', 'ಈ': 'ī', 'ಉ': 'u', 'ಊ': 'ū', 'ಋ': 'r̥',
            'ಎ': 'e', 'ಏ': 'ē', 'ಐ': 'ai', 'ಒ': 'o', 'ಓ': 'ō', 'ಔ': 'au',
            'ಕ': 'k', 'ಖ': 'kh', 'ಗ': 'g', 'ಘ': 'gh', 'ಙ': 'ṅ',
            'ಚ': 'c', 'ಛ': 'ch', 'ಜ': 'j', 'ಝ': 'jh', 'ಞ': 'ñ',
            'ಟ': 'ṭ', 'ಠ': 'ṭh', 'ಡ': 'ḍ', 'ಢ': 'ḍh', 'ಣ': 'ṇ',
            'ತ': 't', 'ಥ': 'th', 'ದ': 'd', 'ಧ': 'dh', 'ನ': 'n',
            'ಪ': 'p', 'ಫ': 'ph', 'ಬ': 'b', 'ಭ': 'bh', 'ಮ': 'm',
            'ಯ': 'y', 'ರ': 'r', 'ಲ': 'l', 'ವ': 'v', 'ಶ': 'ś',
            'ಷ': 'ṣ', 'ಸ': 's', 'ಹ': 'h', 'ಳ': 'ḷ', 'ಕ್ಷ': 'kṣ',
            'ಜ್ಞ': 'jñ',
            'ಾ': 'ā', 'ಿ': 'i', 'ೀ': 'ī', 'ು': 'u', 'ೂ': 'ū', 'ೃ': 'r̥',
            'ೆ': 'e', 'ೇ': 'ē', 'ೈ': 'ai', 'ೊ': 'o', 'ೋ': 'ō', 'ೌ': 'au',
            'ಂ': 'ṁ', 'ಃ': 'ḥ', '್': '',
            '೦': '0', '೧': '1', '೨': '2', '೩': '3', '೪': '4',
            '೫': '5', '೬': '6', '೭': '7', '೮': '8', '೯': '9'
        }

    elif style == 'casual':
        transliteration_map = {
            'ಅ': 'a', 'ಆ': 'a', 'ಇ': 'i', 'ಈ': 'i', 'ಉ': 'u', 'ಊ': 'i', 'ಋ': 'ru',
            'ಎ': 'e', 'ಏ': 'e', 'ಐ': 'ai', 'ಒ': 'o', 'ಓ': 'o', 'ಔ': 'au',
            'ಕ': 'k', 'ಖ': 'kh', 'ಗ': 'g', 'ಘ': 'gh', 'ಙ': 'ng',
            'ಚ': 'ch', 'ಛ': 'cha', 'ಜ': 'j', 'ಝ': 'jh', 'ಞ': 'ny',
            'ಟ': 't', 'ಠ': 'th', 'ಡ': 'd', 'ಢ': 'dh', 'ಣ': 'n',
            'ತ': 't', 'ಥ': 'th', 'ದ': 'd', 'ಧ': 'dh', 'ನ': 'n',
            'ಪ': 'p', 'ಫ': 'ph', 'ಬ': 'b', 'ಭ': 'bh', 'ಮ': 'm',
            'ಯ': 'y', 'ರ': 'r', 'ಲ': 'l', 'ವ': 'v', 'ಶ': 'sh',
            'ಷ': 'sh', 'ಸ': 's', 'ಹ': 'h', 'ಳ': 'l', 'ಕ್ಷ': 'ksh',
            'ಜ್ಞ': 'jn',
            'ಾ': 'a', 'ಿ': 'i', 'ೀ': 'i', 'ು': 'u', 'ೂ': 'u', 'ೃ': 'ru',
            'ೆ': 'e', 'ೇ': 'e', 'ೈ': 'ai', 'ೊ': 'o', 'ೋ': 'o', 'ೌ': 'au',
            'ಂ': 'm', 'ಃ': 'h', '್': '',
            '೦': '0', '೧': '1', '೨': '2', '೩': '3', '೪': '4',
            '೫': '5', '೬': '6', '೭': '7', '೮': '8', '೯': '9'
        }

    else:
        transliteration_map = {
            'ಅ': 'a', 'ಆ': 'aa', 'ಇ': 'i', 'ಈ': 'ee', 'ಉ': 'u', 'ಊ': 'oo', 'ಋ': 'ru',
            'ಎ': 'e', 'ಏ': 'e', 'ಐ': 'ai', 'ಒ': 'o', 'ಓ': 'o', 'ಔ': 'au',
            'ಕ': 'k', 'ಖ': 'kh', 'ಗ': 'g', 'ಘ': 'gh', 'ಙ': 'ng',
            'ಚ': 'ch', 'ಛ': 'chha', 'ಜ': 'j', 'ಝ': 'jh', 'ಞ': 'ny',
            'ಟ': 't', 'ಠ': 'th', 'ಡ': 'd', 'ಢ': 'dh', 'ಣ': 'n',
            'ತ': 't', 'ಥ': 'th', 'ದ': 'd', 'ಧ': 'dh', 'ನ': 'n',
            'ಪ': 'p', 'ಫ': 'ph', 'ಬ': 'b', 'ಭ': 'bh', 'ಮ': 'm',
            'ಯ': 'y', 'ರ': 'r', 'ಲ': 'l', 'ವ': 'v', 'ಶ': 'sh',
            'ಷ': 'sh', 'ಸ': 's', 'ಹ': 'h', 'ಳ': 'l', 'ಕ್ಷ': 'ksh',
            'ಜ್ಞ': 'jn',
            'ಾ': 'aa', 'ಿ': 'i', 'ೀ': 'ee', 'ು': 'u', 'ೂ': 'oo', 'ೃ': 'ru',
            'ೆ': 'e', 'ೇ': 'e', 'ೈ': 'ai', 'ೊ': 'o', 'ೋ': 'o', 'ೌ': 'au',
            'ಂ': 'm', 'ಃ': 'h', '್': '',
            '೦': '0', '೧': '1', '೨': '2', '೩': '3', '೪': '4',
            '೫': '5', '೬': '6', '೭': '7', '೮': '8', '೯': '9'
        }

    # Define sets of characters for logic
    kannada_vowels = set('ಅಆಇಈಉಊಋಎಏಐಒಓಔ')
    kannada_consonants = set('ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳ')
    kannada_vowel_signs = set('ಾಿೀುೂೃೆೇೈೊೋೌ')
    kannada_virama = '್'

    result = []
    i = 0
    while i < len(text):
        char = text[i]

        # Handle complex conjuncts (e.g., 'ಕ್ಷ')
        if char == 'ಕ' and i + 2 < len(text) and text[i + 1:i + 3] == '್ಷ':
            result.append(transliteration_map.get('ಕ್ಷ', 'ksha'))
            i += 3
            continue

        # Handle consonant followed by a vowel sign
        if char in kannada_consonants and i + 1 < len(text) and text[i + 1] in kannada_vowel_signs:
            result.append(transliteration_map.get(char, '') + transliteration_map.get(text[i + 1], ''))
            i += 2
            continue

        # Handle consonant followed by virama (removes inherent vowel)
        if char in kannada_consonants and i + 1 < len(text) and text[i + 1] == kannada_virama:
            result.append(transliteration_map.get(char, ''))
            i += 2
            continue

        # Handle independent vowels and other characters
        if char in kannada_vowels or char not in kannada_consonants:
            result.append(transliteration_map.get(char, char))
            i += 1
            continue

        # Default case for consonants (adds inherent 'a')
        if char in kannada_consonants:
            result.append(transliteration_map.get(char, '') + 'a')
            i += 1

    return "".join(result)