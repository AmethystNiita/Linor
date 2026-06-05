def transliterate_syriac(text):
    chars = {
        # Consonants
    "ܐ": "ʾ", "ܒ": "b", "ܓ": "g", "ܕ": "d", "ܗ": "h", "ܘ": "w", "ܙ": "z", "ܚ": "ḥ",
    "ܛ": "ṭ", "ܝ": "y", "ܟ": "k", "ܠ": "l", "ܡ": "m", "ܢ": "n", "ܣ": "s", "ܥ": "ʿ",
    "ܦ": "p", "ܨ": "ṣ", "ܩ": "q", "ܪ": "r", "ܫ": "š", "ܬ": "t",

    # Modified consonants
    "ܟ݂": "kh", "ܓ݂": "gh", "ܒ݂": "v", "ܦ݂": "f", "ܬ݂": "th", "ܕ݂": "dh",

    # Diacritics
    "ܳ": "ā",
    "ܲ": "a",
    "ܶ": "ē",
    "ܸ": "i",
    "ܺ": "ī",
    "ܿ": "u",
    "ܽ": "ū",

    # Other diacritics
    "ܼ": "",
    "݂": "",
    "݁": "",
    "ّ": "",
    "ْ": "",
    "ܞ": ""
    }

    result = ""
    for char in text:
        result += chars.get(char, char)
    return result