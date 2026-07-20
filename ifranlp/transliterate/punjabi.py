import re


def transliterate_punjabi(text, style='standard'):
    # --- 1. Formal Mapping (Precise dots and macrons) ---
    formal_mapping = {
        'ੜ੍ਹ': 'ṛh', 'ਖ਼': 'x', 'ਗ਼': 'ġ', 'ਸ਼': 'ś', 'ਜ਼': 'z', 'ਫ਼': 'f', 'ਲ਼': 'ḷ',
        '੍ਹ': 'h', '੍ਰ': 'r', '੍ਵ': 'v', '੍ਯ': 'y',
        'ਅ': 'a', 'ਆ': 'ā', 'ਇ': 'i', 'ਈ': 'ī', 'ਉ': 'u', 'ਊ': 'ū', 'ਏ': 'e', 'ਐ': 'ai', 'ਓ': 'o', 'ਔ': 'au',
        'ੳ': '', 'ੲ': '',
        'ਕ': 'k', 'ਖ': 'kh', 'ਗ': 'g', 'ਘ': 'gh', 'ਙ': 'ṅ',
        'ਚ': 'c', 'ਛ': 'ch', 'ਜ': 'j', 'ਝ': 'jh', 'ਞ': 'ñ',
        'ਟ': 'ṭ', 'ਠ': 'ṭh', 'ਡ': 'ḍ', 'ਢ': 'ḍh', 'ਣ': 'ṇ',
        'ਤ': 't', 'ਥ': 'th', 'ਦ': 'd', 'ਧ': 'dh', 'ਨ': 'n',
        'ਪ': 'p', 'ਫ': 'ph', 'ਬ': 'b', 'ਭ': 'bh', 'ਮ': 'm',
        'ਯ': 'y', 'ਰ': 'r', 'ਲ': 'l', 'ਵ': 'v', 'ੜ': 'ṛ',
        'ਸ': 's', 'ਹ': 'h',
        'ਾ': 'ā', 'ਿ': 'i', 'ੀ': 'ī', 'ੁ': 'u', 'ੂ': 'ū', 'ੇ': 'e', 'ੈ': 'ai', 'ੋ': 'o', 'ੌ': 'au',
        'ਂ': 'ṃ', 'ੰ': 'ṃ', '੍': '', '਼': '', '।': '.', '॥': '.',
        '੦': '0', '੧': '1', '੨': '2', '੩': '3', '੪': '4', '੫': '5', '੬': '6', '੭': '7', '੮': '8', '੯': '9',
        'ੴ': 'ik ōaṅkār', 'ਃ': 'h'
    }

    # --- 2. Casual Mapping (Relaxed SMS style) ---
    casual_mapping = {
        'ੜ੍ਹ': 'rh', 'ਖ਼': 'kh', 'ਗ਼': 'g', 'ਸ਼': 'sh', 'ਜ਼': 'z', 'ਫ਼': 'f', 'ਲ਼': 'l',
        '੍ਹ': 'h', '੍ਰ': 'r', '੍ਵ': 'v', '੍ਯ': 'y',
        'ਅ': 'a', 'ਆ': 'a', 'ਇ': 'i', 'ਈ': 'i', 'ਉ': 'u', 'ਊ': 'u', 'ਏ': 'e', 'ਐ': 'ai', 'ਓ': 'o', 'ਔ': 'au',
        'ੳ': '', 'ੲ': '',
        'ਕ': 'k', 'ਖ': 'kh', 'ਗ': 'g', 'ਘ': 'gh', 'ਙ': 'ng',
        'ਚ': 'ch', 'ਛ': 'chh', 'ਜ': 'j', 'ਝ': 'jh', 'ਞ': 'ny',
        'ਟ': 't', 'ਠ': 'th', 'ਡ': 'd', 'ਢ': 'dh', 'ਣ': 'n',
        'ਤ': 't', 'ਥ': 'th', 'ਦ': 'd', 'ਧ': 'dh', 'ਨ': 'n',
        'ਪ': 'p', 'ਫ': 'f', 'ਬ': 'b', 'ਭ': 'bh', 'ਮ': 'm',
        'ਯ': 'y', 'ਰ': 'r', 'ਲ': 'l', 'ਵ': 'v', 'ੜ': 'r',
        'ਸ': 's', 'ਹ': 'h',
        'ਾ': 'a', 'ਿ': 'i', 'ੀ': 'i', 'ੁ': 'u', 'ੂ': 'u', 'ੇ': 'e', 'ੈ': 'ai', 'ੋ': 'o', 'ੌ': 'au',
        'ਂ': 'n', 'ੰ': 'n', '੍': '', '਼': '', '।': '.', '॥': '.',
        '੦': '0', '੧': '1', '੨': '2', '੩': '3', '੪': '4', '੫': '5', '੬': '6', '੭': '7', '੮': '8', '੯': '9',
        'ੴ': 'ik onkar', 'ਃ': 'h'
    }

    # --- 3. Standard Mapping ---
    standard_mapping = {
        'ੜ੍ਹ': 'rh', 'ਖ਼': 'kh', 'ਗ਼': 'g', 'ਸ਼': 'sh', 'ਜ਼': 'z', 'ਫ਼': 'ph', 'ਲ਼': 'l',
        '੍ਹ': 'h', '੍ਰ': 'r', '੍ਵ': 'v', '੍ਯ': 'y',
        'ਅ': 'a', 'ਆ': 'aa', 'ਇ': 'i', 'ਈ': 'ee', 'ਉ': 'u', 'ਊ': 'oo', 'ਏ': 'e', 'ਐ': 'ai', 'ਓ': 'o', 'ਔ': 'au',
        'ੳ': '', 'ੲ': '',
        'ਕ': 'k', 'ਖ': 'kh', 'ਗ': 'g', 'ਘ': 'gh', 'ਙ': 'ng',
        'ਚ': 'ch', 'ਛ': 'ch', 'ਜ': 'j', 'ਝ': 'jh', 'ਞ': 'ny',
        'ਟ': 't', 'ਠ': 'th', 'ਡ': 'd', 'ਢ': 'dh', 'ਣ': 'n',
        'ਤ': 't', 'ਥ': 'th', 'ਦ': 'd', 'ਧ': 'dh', 'ਨ': 'n',
        'ਪ': 'p', 'ਫ': 'ph', 'ਬ': 'b', 'ਭ': 'bh', 'ਮ': 'm',
        'ਯ': 'y', 'ਰ': 'r', 'ਲ': 'l', 'ਵ': 'v', 'ੜ': 'r',
        'ਸ': 's', 'ਹ': 'h',
        'ਾ': 'a', 'ਿ': 'i', 'ੀ': 'ee', 'ੁ': 'u', 'ੂ': 'oo', 'ੇ': 'e', 'ੈ': 'ai', 'ੋ': 'o', 'ੌ': 'au',
        'ਂ': 'n', 'ੰ': 'n', '੍': '', '਼': '', '।': '.', '॥': '.',
        '੦': '0', '੧': '1', '੨': '2', '੩': '3', '੪': '4', '੫': '5', '੬': '6', '੭': '7', '੮': '8', '੯': '9',
        'ੴ': 'ik oankar', 'ਃ': 'h'
    }

    if style == 'formal':
        active_mapping = formal_mapping
    elif style == 'casual':
        active_mapping = casual_mapping
    else:
        active_mapping = standard_mapping

    consonants = 'ਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਲ਼ਵੜਸ਼ਖ਼ਗ਼ਜ਼ਫ਼ਸਹ'
    independent_vowels = 'ਅਆਇਈਉਊਏਐਓਔੳੲ'

    # --- PHASE 0: Normalization & Keyboard Quirks ---
    # Fixes base vowel + matra typos
    text = text.replace('ਅਾ', 'ਆ').replace('ਇਿ', 'ਇ').replace('ਉੁ', 'ਉ')

    # Fixes split Nuqta combinations (forces them into single characters to prevent breaking)
    text = text.replace('ਸ਼', 'ਸ਼').replace('ਖ਼', 'ਖ਼').replace('ਗ਼', 'ਗ਼').replace('ਜ਼', 'ਜ਼').replace('ਫ਼',
                                                                                                        'ਫ਼').replace(
        'ਲ਼', 'ਲ਼')

    # Matches Google Translate's formatting for the word "'ਤੇ" (utte/on)
    text = text.replace(" 'ਤੇ", "'ਤੇ")

    # --- PHASE 1: Syllable Separation (Apostrophes for Vowels) ---
    # Injects an apostrophe before independent vowels found inside a word (e.g. ਕਿਉਂ -> ਕਿ'ਉਂ -> ki'uṃ)
    # \u0A00-\u0A7F ensures it only triggers if preceded by another Gurmukhi character
    text = re.sub(f'(?<=[\u0A00-\u0A7F])([{independent_vowels}])', r"'\1", text)

    # --- PHASE 2: Smart Implicit 'a' Spacing (Schwa) ---
    # Adds 'a' if a consonant is followed by another consonant, Adhak, Tippi, or Bindi.
    # We do this BEFORE Adhak expansion so words like "hadd" don't get starved of their vowel!
    text = re.sub(f'([{consonants}])(?=[{consonants}ੱੰਂ])', r'\1a', text)

    # --- PHASE 3: Expand the Adhak (ੱ) ---
    def duplicate_consonant(match):
        return match.group(1) + match.group(1)

    text = re.sub(f'ੱ([{consonants}])', duplicate_consonant, text)

    # --- PHASE 4: Context-Aware Nasalization ---
    # Tippi/Bindi become 'm' when followed by Labial consonants
    labials = 'ਪਫਬਭਮ'
    text = re.sub(f'[ਂੰ](?=[{labials}])', 'm', text)

    # --- PHASE 5: Transliterate ---
    for punjabi_char, latin_char in active_mapping.items():
        text = text.replace(punjabi_char, latin_char)

    return text