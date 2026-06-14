def transliterate_syriac(text):
    # 1. Handle multi-character combinations first so they don't get split up
    multi_chars = {
        "ܟ݂": "kh",
        "ܓ݂": "gh",
        "ܒ݂": "v",
        "ܦ݂": "f",
        "ܬ݂": "th",
        "ܕ݂": "dh"
    }

    for syriac_pair, english_sound in multi_chars.items():
        text = text.replace(syriac_pair, english_sound)

    # 2. Handle single characters (individual letters and vowels)
    single_chars = {
        # Consonants
        "ܐ": "ʾ", "ܒ": "b", "ܓ": "g", "ܕ": "d", "ܗ": "h", "ܘ": "w", "ܙ": "z", "ܚ": "ḥ",
        "ܛ": "ṭ", "ܝ": "y", "ܟ": "k", "ܠ": "l", "ܡ": "m", "ܢ": "n", "ܣ": "s", "ܥ": "ʿ",
        "ܦ": "p", "ܨ": "ṣ", "ܩ": "q", "ܪ": "r", "ܫ": "š", "ܬ": "t",

        # Diacritics / Vowels (Standard Nestorian/Western values)
        "ܳ": "ā",
        "ܲ": "a",
        "ܶ": "ē",
        "ܸ": "i",
        "ܺ": "ī",
        "ܿ": "u",
        "ܽ": "ū",
        "ܵ": "ā",  # Horizontal Zqapa
        "ܹ": "ē",  # Zlama pshiqu

        # Miscellaneous markers to smoothly ignore
        "ܼ": "",
        "݂": "",  # Cleans up any stray independent rukkakha dots
        "݁": "",  # Qushshaya (hard dot)
        "ّ": "",
        "ْ": "",
        "ܞ": "yh"  # Jah (traditional abbreviation symbol for Lord)
    }

    # 3. Translate the remaining characters
    result = ""
    for char in text:
        result += single_chars.get(char, char)

    return result