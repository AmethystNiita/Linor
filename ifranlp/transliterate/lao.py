def transliterate_lao(text):
    mapping = {
        'ກ': 'k', 'ຂ': 'kh', 'ຄ': 'kh', 'ງ': 'ng', 'ຈ': 'ch', 'ຊ': 's', 'ສ': 's',
        'ຍ': 'ny', 'ດ': 'd', 'ຕ': 't', 'ຖ': 'th', 'ທ': 'th', 'ນ': 'n',
        'ບ': 'b', 'ປ': 'p', 'ຜ': 'ph', 'ຝ': 'f', 'ພ': 'ph', 'ຟ': 'f', 'ມ': 'm',
        'ຢ': 'y', 'ຣ': 'r', 'ລ': 'l', 'ວ': 'v', 'ອ': 'o', 'ຫ': 'h', 'ຬ': 's',
        'ຯ': '',

        'ະ': 'a', 'າ': 'aa', 'ິ': 'i', 'ີ': 'ii', 'ຶ': 'eu', 'ື': 'euu',
        'ຸ': 'u', 'ູ': 'uu', '່': '', '້': '', '໊': '', '໋': '', '໌': '',
        'ເ': 'e', 'ແ': 'ae', 'ໂ': 'o', 'ໃ': 'ai', 'ໄ': 'ai', 'ົ': 'o', 'ຽ': 'ia',

        ' ': ' ', 'ໆ': ' ', 'ຫຼ': 'hl', '຺': '',
    }

    transliterated_text = ''
    for char in text:
        transliterated_char = mapping.get(char, char)
        transliterated_text += transliterated_char
    return transliterated_text