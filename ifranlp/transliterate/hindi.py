import re
from num2words import num2words

def transliterate_hindi(text, number_style='keep', style='standard'):
    # --- 1. Formal Mapping (Proper macrons and retroflex dots) ---
    formal_mapping = {
        'ेई': 'ei', 'ज़': 'z', 'ड़': 'ṛ', 'ढ़': 'ṛh',
        'अ': 'a', 'आ': 'ā', 'ऑ': 'o', 'इ': 'i', 'ई': 'ī', 'उ': 'u', 'ऊ': 'ū', 'ऋ': 'ṛ', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
        'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ṅ',
        'च': 'c', 'छ': 'ch', 'ज': 'j', 'झ': 'jh', 'ञ': 'ñ',
        'ट': 'ṭ', 'ठ': 'ṭh', 'ड': 'ḍ', 'ढ': 'ḍh', 'ण': 'ṇ',
        'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
        'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
        'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v',
        'श': 'ś', 'ष': 'ṣ', 'स': 's', 'ह': 'h',
        'ः': 'ḥ', 'ं': 'ṃ', 'ँ': 'm̐',
        'ा': 'ā', 'ि': 'i', 'ी': 'ī', 'ु': 'u', 'ू': 'ū', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ॉ': 'o', 'ौ': 'au', 'ृ': 'ṛ',
        '।': '.', '्': '', '़': '',
        '०': '0', '१': '1', '२': '2', '३': '3', '४': '4', '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
    }

    # --- 2. Casual Mapping (Relaxed SMS style, no vowel distinctions) ---
    casual_mapping = {
        'ेई': 'ei', 'ज़': 'z',
        'अ': 'a', 'आ': 'a', 'ऑ': 'o', 'इ': 'i', 'ई': 'i', 'उ': 'u', 'ऊ': 'u', 'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
        'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh',
        'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
        'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
        'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
        'प': 'p', 'फ': 'f', 'ब': 'b', 'भ': 'bh', 'म': 'm',
        'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v',
        'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
        'ः': 'h', 'ं': 'n', 'ँ': 'n',
        'ा': 'a', 'ि': 'i', 'ी': 'i', 'ु': 'u', 'ू': 'u', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ॉ': 'o', 'ौ': 'au', 'ृ': 'ri',
        '।': '.', '्': '', '़': '',
        '०': '0', '१': '1', '२': '2', '३': '3', '४': '4', '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
    }

    # --- 3. Standard Mapping (Your original setup) ---
    standard_mapping = {
        'ेई': 'ei', 'ज़': 'z',
        'अ': 'a', 'आ': 'aa', 'ऑ': 'o', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'r', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
        'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh',
        'च': 'ch', 'छ': 'ch', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
        'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
        'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
        'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
        'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v',
        'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
        'ः': 'h', 'ं': 'n', 'ँ': 'n',
        'ा': 'a', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'uu', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ॉ': 'o', 'ौ': 'au', 'ृ': 'r',
        '।': '.', '्': '', '़': '',
        '०': '0', '१': '1', '२': '2', '३': '3', '४': '4', '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
    }

    # Select the style map
    if style == 'formal':
        active_mapping = formal_mapping
    elif style == 'casual':
        active_mapping = casual_mapping
    else:
        active_mapping = standard_mapping

    def number_to_words(match):
        number = int(match.group())
        return num2words(number, lang='hi')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    # Insert implicit 'a' between adjacent consonants
    consonants = 'कखगघचछजझञटठडढतथदधनपफबभमयरलवशषसह'
    text = re.sub(f'([{consonants}])(?=[{consonants}])', r'\1a', text)

    # Apply the selected transliteration dictionary
    # (Because Python dictionaries preserve order, double characters like 'ेई' stay perfectly safe at the top!)
    for hindi_char, latin_char in active_mapping.items():
        text = text.replace(hindi_char, latin_char)

    return text