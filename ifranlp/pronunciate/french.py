from num2words import num2words
import re

def pronunciate_french(text, style='standard', number_style='keep'):
    if style == 'casual':
        french_exceptions = [
            # Common endings
            (r'ent\b', 'ahn'),  # parlent → parlahn
            (r'eux\b', 'uh'),  # heureux → uhruh
            (r'tion\b', 'syon'),  # nation → nasyon
            (r'ssion\b', 'syon'),  # mission → misyon
            (r'ien\b', 'yen'),  # bien → byen
            (r'ienn\b', 'yen'),  # ancienne → ah-syen
            (r'ais\b', 'ay'),  # fais → fay
            (r'ait\b', 'ay'),  # faisait → fuh-zay
            (r'aît\b', 'ay'),  # connaît → koh-nay
            (r'ez\b', 'ay'),  # parlez → parlay
            (r'aux\b', 'oh'),  # chevaux → shuh-voh
            (r'eau\b', 'oh'),  # beau → boh
            (r'eaux\b', 'oh'),  # bateaux → ba-toh
            (r'ot\b', 'oh'),  # mot → moh
            (r'ots\b', 'oh'),  # mots → moh

            # Nasal vowels (English approximations)
            (r'ain', 'ang'),
            (r'aim', 'ang'),
            (r'an', 'ahn'),
            (r'am', 'ahm'),
            (r'en', 'ahn'),
            (r'em', 'ahm'),
            (r'on', 'ong'),
            (r'om', 'om'),
            (r'in', 'ang'),
            (r'im', 'ang'),
            (r'yn', 'ang'),
            (r'un', 'uhn'),

            # Special consonants
            (r'ch', 'sh'),
            (r'gn', 'ny'),
            (r'ph', 'f'),
            (r'th', 't'),
            (r'ill', 'y'),  # famille → fa-mee-y

            # Vowel combos
            (r'oi', 'wah'),
            (r'ou', 'oo'),
            (r'au', 'oh'),
            (r'eau', 'oh'),
            (r'qu', 'k'),

            # Soft consonants
            (r'ç', 's'),
            (r'c(?=[eéi])', 's'),
            (r'c', 'k'),
            (r'g(?=[eéi])', 'zh'),
            (r'ge', 'zhuh'),
            (r'g', 'g'),

            # Misc silent letters
            (r'h', ''),  # silent h
            (r's\b', ''),  # final s
            (r't\b', ''),  # final t
            (r'd\b', ''),  # final d
            (r'p\b', ''),  # final p
            (r'x\b', ''),  # final x
        ]

    else:
        french_exceptions = [
            # Common endings (whole words or suffixes)
            (r'ent\b', 'ã'),       # ils parlent → parlã
            (r'eux\b', 'ø'),       # heureux → øʁø
            (r'tion\b', 'syon'),   # nation → nasyon
            (r'ssion\b', 'syon'),  # mission → misyon
            (r'ien\b', 'jɛ̃'),     # bien → bjɛ̃
            (r'ienn\b', 'jɛn'),    # ancienne → asjɛn
            (r'ais\b', 'ɛ'),       # je fais → fe
            (r'ait\b', 'ɛ'),       # il faisait → fəzɛ
            (r'aît\b', 'ɛ'),       # connaît → konɛ
            (r'ez\b', 'e'),        # vous parlez → parle
            (r'aux\b', 'o'),       # chevaux → ʃəvo
            (r'eau\b', 'o'),       # beau → bo
            (r'eaux\b', 'o'),      # bateaux → bato
            (r'ot\b', 'o'),        # mot → mo
            (r'ots\b', 'o'),       # mots → mo

            # Nasal vowels
            (r'an', 'ã'),
            (r'en', 'ã'),
            (r'on', 'õ'),
            (r'in', 'ɛ̃'),
            (r'ain', 'ɛ̃'),
            (r'yn', 'ɛ̃'),
            (r'un', 'œ̃'),

            # Special consonants
            (r'ch', 'ʃ'),
            (r'gn', 'ɲ'),
            (r'ph', 'f'),
            (r'th', 't'),
            (r'ill', 'j'),   # famille → famij

            # Vowels and combos
            (r'oi', 'wa'),
            (r'ou', 'u'),
            (r'au', 'o'),
            (r'eau', 'o'),
            (r'qu', 'k'),

            # Soft consonants
            (r'ç', 's'),
            (r'c(?=[eéi])', 's'),
            (r'c', 'k'),
            (r'g(?=[eéi])', 'ʒ'),
            (r'ge', 'ʒə'),
            (r'g', 'g'),

            # Misc silent letters
            (r'h', ''),    # h is silent
            (r's\b', ''),  # final s silent
            (r't\b', ''),  # final t silent
            (r'd\b', ''),  # final d silent
            (r'p\b', ''),  # final p silent
            (r'x\b', ''),  # final x silent
        ]

    def number_to_french_words(match):
        number = int(match.group())
        return num2words(number, lang='fr')

    def replace_numbers_with_words(txt):
        return re.sub(r'\b\d+\b', number_to_french_words, txt)

    if number_style == 'words':
        text = replace_numbers_with_words(text)

    # apply replacements in order
    for pattern, repl in french_exceptions:
        text = re.sub(pattern, repl, text)

    return text
