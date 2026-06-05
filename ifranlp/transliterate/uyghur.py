def transliterate_uyghur(text):
    mapping = {
        # Consonants with unique Latin mappings
        "غ": "gh",
        "ش": "sh",
        "چ": "ch",
        "ژ": "zh",
        "ڭ": "ng",

        # Vowels (Context-dependent or simple mapping)
        "ې": "ë",  # E with diaeresis (used for /e/)
        "ۆ": "ö",  # O with diaeresis (used for /ø/)
        "ۈ": "ü",  # U with diaeresis (used for /y/)

        # Standard Consonants
        "ب": "b", "پ": "p", "ت": "t", "ج": "j",
        "خ": "x", "د": "d", "ر": "r", "ز": "z",
        "س": "s", "ف": "f", "ق": "q", "ك": "k",
        "گ": "g", "ل": "l", "م": "m", "ن": "n",
        "ھ": "h", "ي": "y", "و": "w",

        # Vowels (Simplified/Contextual)
        "ا": "a",
        "ە": "e",
        "و": "o",
        "ئ": "\'",  # Alif/Hamza often transliterated as 'i' or omitted/used for initial vowel
        "ۇ": "u",
        "ى": "i",
        "ۋ": 'w',

        # Special/Contextual (Handle initial Alif with Hamza)
        # Note: Initial 'ﺋا' (A) is the most complex part of Uyghur transliteration.
        # Simple Arabic Alif-Hamza 'ئ' is handled above for simplicity.

        # Arabic-specific (rare in native Uighur words)
        "ع": "’",  # Ain
        "ث": "s",  # Tha (often transliterated as s)
        "ذ": "z",  # Dhal (often transliterated as z)
        "ص": "s",  # Sad
        "ض": "z",  # Dad (often transliterated as z)
        "ط": "t",  # Ta
        "ظ": "z",  # Za

        # Word separators/Punctuation
        "،": ",",
        "؟": "?",
        # ... add others
    }

    # 2. Perform the Substitutions
    transliterated_text = text
    for uey, uly in mapping.items():
        transliterated_text = transliterated_text.replace(uey, uly)

    return transliterated_text