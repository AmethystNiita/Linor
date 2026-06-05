def transliterate_greek(text):
    greek_transliteration = {
        'α': 'a',
        'ά': 'á',
        'β': 'v',
        'γ': 'g',
        'δ': 'd',
        'ε': 'e',
        'έ': 'é',
        'ζ': 'z',
        'η': 'i',
        'ή': 'í',
        'θ': 'th',
        'ι': 'i',
        'ί': 'í',
        'ϊ': 'ï',
        'ΐ': 'ḯ',
        'κ': 'k',
        'λ': 'l',
        'μ': 'm',
        'ν': 'n',
        'ξ': 'x',
        'ο': 'o',
        'ό': 'ó',
        'π': 'p',
        'ρ': 'r',
        'σ': 's',
        'ς': 's',
        'τ': 't',
        'υ': 'y',
        'ύ': 'ý',
        'ϋ': 'ÿ',
        'ΰ': 'ÿ́',
        'φ': 'f',
        'χ': 'ch',
        'ψ': 'ps',
        'ω': 'o',
        'ώ': 'ó',
        # Add more mappings as needed
    }

    transliterated_text = ''
    for char in text:
        transliterated_char = greek_transliteration.get(char.lower(), char)
        if char.isupper():
            transliterated_char = transliterated_char.capitalize()
        transliterated_text += transliterated_char

    transliterated_text = transliterated_text.replace('oy', 'ou')
    transliterated_text = transliterated_text.replace('mp', 'b')
    transliterated_text = transliterated_text.replace('aý', 'av')
    transliterated_text = transliterated_text.replace('ay', 'af')
    transliterated_text = transliterated_text.replace('mp', 'b')
    return transliterated_text
