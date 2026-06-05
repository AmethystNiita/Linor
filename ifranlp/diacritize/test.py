def segment_arabic(word: str) -> list[str]:
    """
    Segments an Arabic word by splitting off common prefixes and suffixes.

    This is a rule-based morphological segmenter, not a true lemmatizer.
    It works well for common clitics but may not cover all complex grammatical cases.

    Args:
        word: The Arabic word to segment.

    Returns:
        A list of strings containing the segmented parts (prefixes, stem, suffixes).
    """
    # Define prefixes and suffixes. Order can be important.
    # We check for 'ال' separately, then iterative single-character prefixes.
    PREFIXES = ['ال', 'و', 'ف', 'ب', 'ك', 'ل', 'أ']
    # Suffixes are ordered by a potential stripping order.
    # Pronoun suffixes and common plural/dual markers.
    SUFFIXES = ['ها', 'هم', 'هن', 'ك', 'كم', 'كن', 'ي', 'نا', 'وا', 'ون', 'ين', 'ان', 'ات', 'ت', 'ة']
    # Vowels that sometimes connect suffixes and need to be removed.
    JOINER_VOWELS = ['و', 'ي']

    original_word = word
    prefixes = []
    suffixes = []

    # 1. Prefix Stripping
    # First, handle the definite article 'ال'
    if original_word.startswith('ال'):
        prefixes.append('ال')
        original_word = original_word[2:]

    # Then, handle single-character conjunctions, prepositions, etc.
    # We loop to catch multiple prefixes like 'وأل' or 'فب'
    while len(original_word) > 2:
        found = False
        for p in PREFIXES:
            # Skip 'ال' since we already handled it
            if p == 'ال':
                continue
            if original_word.startswith(p):
                prefixes.append(p)
                original_word = original_word[len(p):]
                found = True
                break # Restart the check for the new shortened word
        if not found:
            break

    stem = original_word

    # 2. Suffix Stripping (from the end of the word)
    while len(stem) > 2:
        found = False
        for s in SUFFIXES:
            if stem.endswith(s):
                suffixes.insert(0, s) # Add to the beginning to maintain order
                stem = stem[:-len(s)]
                # **Special rule**: After stripping a pronoun, if the stem
                # now ends in a joiner vowel, remove it. This handles cases
                # like 'كموها' -> 'كمو' -> 'كم'.
                if len(stem) > 0 and stem[-1] in JOINER_VOWELS:
                    stem = stem[:-1]
                found = True
                break # Restart the check for the new shortened stem
        if not found:
            break

    # 3. Combine and return
    return prefixes + [stem] + suffixes

# --- Examples ---
word1 = "السلام"
word2 = "أفإستسقيناكموها"
word3 = "وبالمكتبة" # Another example: And in the library
word4 = "وبصراحة"

print(f'"{word1}" -> {segment_arabic(word1)}')
print(f'"{word2}" -> {segment_arabic(word2)}')
print(f'"{word3}" -> {segment_arabic(word3)}')
print(f'"{word4}" -> {segment_arabic(word4)}')