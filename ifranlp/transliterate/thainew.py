import pythainlp
from num2words import num2words
import re
from pythainlp.util import maiyamok

# Dictionaries and rules are defined once for all functions
thai_transliteration = {
    'ก': 'k', 'ข': 'kh', 'ฃ': 'kh', 'ค': 'kh', 'ฅ': 'kh', 'ฆ': 'kh',
    'ง': 'ng', 'จ': 'j', 'ฉ': 'ch', 'ช': 'ch', 'ซ': 's', 'ฌ': 'ch',
    'ญ': 'y', 'ฎ': 'd', 'ฏ': 't', 'ฐ': 'th', 'ฑ': 'th', 'ฒ': 'th',
    'ณ': 'n', 'ด': 'd', 'ต': 't', 'ถ': 'th', 'ท': 'th', 'ธ': 'th',
    'น': 'n', 'บ': 'b', 'ป': 'p', 'ผ': 'ph', 'ฝ': 'f', 'พ': 'ph',
    'ฟ': 'f', 'ภ': 'ph', 'ม': 'm', 'ย': 'y', 'ร': 'r', 'ล': 'l',
    'ว': 'w', 'ศ': 's', 'ษ': 's', 'ส': 's', 'ห': 'h', 'ฬ': 'l',
    'อ': 'o', 'ฮ': 'h', 'ะ': 'a', 'ั': 'a', 'า': 'a', 'ิ': 'i',
    'ี': 'ee', 'ึ': 'ue', 'ื': 'ue', 'ุ': 'u', 'ู': 'oo', 'เ': 'e',
    'แ': 'ae', 'โ': 'o', 'ใ': 'ai', 'ไ': 'ai', 'ำ': 'am', '่': '',
    '้': '', '๊': '', '๋': '', '็': '', '์': '', 'ๆ': '', 'ํ': 'ang',
    'ฤ': 'rue', 'ฦ': 'lue',
    'ຍ': 'y',
    #'\ue000': 'kr', '\ue001': 'khr', '\ue002': 'tr', '\ue003': 'pr',
    #'\ue004': 'phr', '\ue005': 'kl', '\ue006': 'khl', '\ue007': 'pl',
    #'\ue008': 'phl', '\ue009': 'kw', '\ue010': 'khw', '\ue011': 'sr',
    #'\ue012': 's', '\ue013': 'w', '\ue014': '',
    '\ue015': 'ny', 'ຊ': 'x'
}

thai_consonants = (
    'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ',
    'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ล', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'ฮ', 'ຮ', 'ຊ', 'ฤ')

valid_khmer_loans = (
    'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ',
    'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ศ', 'ษ', 'ส', 'ฬ', 'ฮ')

mae_kok = {'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ'}
mae_kon = {'น', 'ร', 'ญ', 'ณ', 'ฬ'}
mae_kod = {'จ', 'ช', 'ซ', 'ฎ', 'ด', 'ศ', 'ษ', 'ส'}
mae_kot = {'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ต', 'ถ', 'ท', 'ธ'}
mae_koei = {'ย'}
thai_vowels = {'ะ', 'ั', 'า', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู', 'เ', 'แ', 'โ', 'ใ', 'ไ', 'ำ', '่', '้', '๊', '๋', '็', '์', 'ๆ'}
thai_vowels_ai_sounds = {'ไ', 'ใ'}
thai_vowels_with_no_ai_sounds = {'ะ', 'ั', 'า', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู', 'เ', 'แ', 'โ', 'ำ', '่', '้', '๊', '๋', '็', '์', 'ๆ'}

karan_combinations = {
    "กดิ์": "ก", "กดิ": "ก", "ทธิ์": "ท", "ทธิ": "ทิ", "นพันธุ์": "น", "นธ์": "น", "นทร์": "น", "นทน์": "น",
    "ภูมิ": "พูม", "ภูมิ์": "พูม", "ตน์": "ต", "สตร์": "ต", "ทย์": "ต", "ศน์": "ต",
    "าธิ": "at", "าติ": "at", "ัติ": "at", "นต์": "น", "นตร์": "น", "งค์": "ง",
    "ก์": "", "ข์": "", "ค์": "", "ฆ์": "", "ง์": "", "จ์": "", "ฉ์": "", "ช์": "",
    "ซ์": "", "ฌ์": "", "ญ์": "", "ฎ์": "", "ฏ์": "", "ฐ์": "", "ฑ์": "", "ฒ์": "",
    "ณ์": "", "ด์": "", "ต์": "", "ถ์": "", "ท์": "", "ธ์": "", "น์": "", "บ์": "",
    "ป์": "", "ผ์": "", "ฝ์": "", "พ์": "", "ฟ์": "", "ภ์": "", "ม์": "", "ย์": "",
    "ร์": "r", "ล์": "", "ว์": "", "ษ์": "", "ส์": ""
}

ro_rue_lo_lue = {
    'ฤๅ': 'rue', 'ฦๅ': 'lue', 'กฤ': 'kri', 'ตฤ': 'tari', 'ทฤ': 'thari',
    'ปฤ': 'pari', 'ศฤ': 'sri', 'สฤ': 'sri', 'คฤ': 'karue', 'นฤ': 'narue',
    'พฤ': 'pharue', 'มฤ': 'marue', 'หฤ': 'harue'
}

exceptions = { 'ฯลฯ': 'lae uen uen' }
exact_exceptions = { 'ลออ': 'la or', 'บ่': 'bo', 'ก็': 'ko' }
preproprietary_exceptions = { 'ค.ศ.': 'khristsakarad', 'พ.ศ.': 'phuthasakarad', 'คำแหง': 'kam haeng'}

proprietary_exceptions = {
    'แห่ง': 'haeng', 'แหง': 'ngae', 'เสมอ': 'samoe',
    'เสนอ': 'sanoe', 'เพราะ': 'phro', 'เฉพาะ': 'chapor', 'ไหม์': 'haim',
    'อย่า': 'ya', 'อยู่': 'yoo', 'อย่าง': 'yang', 'อยาก': 'yak',
    'โทรศัพท์': 'tora sap', 'เสมือน': 'sameuan', 'โทร': 'to', 'เหว': 'hew',
    'หวง': 'huang', 'หงส์': 'hong', 'บรม': 'borom', 'นคร': 'nakhorn',
    'วิศว': 'witsawa', 'วิศวะ': 'witsawa', 'เสน่ห์': 'sane', 'เสนาะ': 'sanor'
}

compounds = { 'บาร': 'bara', 'พุทธ': "phutha" }

vowel_formats = {
    'ทร-': 'so-',
    # --- 1. Complex Vowels ---
    'เห-ียว': '-iao',    'เ-ียว': '-iao',
    'เห-ือะ': '-uea',    'เ-ือะ': '-uea',
    'เห-ือ_': '-uea_',   'เ-ือ_': '-uea_',
    'เห-ือ': '-uea',     'เ-ือ': '-uea',
    'เห-ียะ': '-ia',     'เ-ียะ': '-ia',
    'เห-ีย_': '-ia_',    'เ-ีย_': '-ia_',
    'เห-ีย': '-ia',      'เ-ีย': '-ia',
    'เห-อว': '-oew',    'เ-อว': '-oew',
    'เห-อะ': '-oe',     'เ-อะ': '-oe',
    'เห-ิ_': '-oe_',     'เ-ิ_': '-oe_',
    'เห-ย': '-oei',     'เ-ย': '-oei',
    'เห-ี_': '-oe_',     'เ-ี_': '-oe_',
    'เห-อ': '-oe',      'เ-อ': '-oe',
    'เห-ี': '-oe',      'เ-ี': '-oe',

    # --- 2. Front Vowels WITH Final Consonants ---
    'เห-_': '-e_',       'เ-_': '-e_',
    'แห-_': '-ae_',      'แ-_': '-ae_',
    'โห-_': '-o_',       'โ-_': '-o_',

    # --- 3. Diphthongs & Special Combos ---
    'แห-ว': '-aew',      'แ-ว': '-aew',
    'โห-ย': '-oi',       'โ-ย': '-oi',
    'เห-า': '-ao',       'เ-า': '-ao',
    'เห-าะ': '-or',      'เ-าะ': '-or',
    'แห-ะ': '-ae',       'แ-ะ': '-ae',
    'โห-ะ': '-o',        'โ-ะ': '-o',
    'เห-ะ': '-e',        'เ-ะ': '-e',

    # --- 4. Lao-Specific Bridges ---
    'เห-ั_': '-e_',       'เ-ั_': '-e_',
    'แห-ั_': '-ae_',      'แ-ั_': '-ae_',
    'ห-ัอ_': '-o_',       '-ัอ_': '-o_',
    'ห-ຽ_': '-ia_',       '-ຽ_': '-ia_',

    # --- 5. Short/Long Vowels with Final Consonants ---
    'ห-ัวะ': '-ua',       '-ัวะ': '-ua',
    'ห-ัว': '-ua',        '-ัว': '-ua',
    'ห-ั_': '-a_',        '-ั_': '-a_',
    'ห-ิว': '-iu',        '-ิว': '-iu',
    'ห-าว': '-ao',        '-าว': '-ao',
    'ห-ุย': '-ui',        '-ุย': '-ui',
    'ห-อย': '-oi',        '-อย': '-oi',
    'ห-วย': '-uai',       '-วย': '-uai',
    'ห-ว_': '-ua_',       '-ว_': '-ua_',
    'ห-าย': '-ai',        '-าย': '-ai',

    # --- 6. Standard Base Vowels ---
    'ห-ำ': '-am',         '-ำ': '-am',
    'ให-': '-ai',         'ใ-': '-ai',
    'ไห-': '-ai',         'ไ-': '-ai',
    'เห-': '-e',          'เ-': '-e',
    'แห-': '-ae',         'แ-': '-ae',
    'โห-': '-o',          'โ-': '-o',
    'ห-า': '-a',          '-า': '-a',
    'ห-ะ': '-a',          '-ะ': '-a',
    'ห-ิ': '-i',          '-ิ': '-i',
    'ห-ี': '-ee',         '-ี': '-ee',
    'ห-ึ': '-ue',         '-ึ': '-ue',
    'ห-ื': '-ue',         '-ื': '-ue',
    'ห-ือ': '-ue',        '-ือ': '-ue',
    'ห-ุ': '-u',          '-ุ': '-u',
    'ห-ู': '-oo',         '-ู': '-oo',
    'ห-อ': '-or',         '-อ': '-or',
    'ห-ว': '-ua',         '-ว': '-ua',

    'ห-า_': '-a_',       '-า_': '-a_',
    'ห-ิ_': '-i_',          '-ิ_': '-i_',
    'ห-ี_': '-ee_',         '-ี_': '-ee_',
    'ห-ึ_': '-ue_',         '-ึ_': '-ue_',
    'ห-ื_': '-ue_',         '-ื_': '-ue_',
    'ห-ุ_': '-u_',          '-ุ_': '-u_',
    'ห-ู_': '-oo_',         '-ู_': '-oo_',
    'ห-อ_': '-or_',        '-อ_': '-or_',
    'ออ-': 'or-',          'ห-_': '-o_'
}

def number_to_thai_words(match):
    number = int(match.group())
    return num2words(number, lang='th')

def replace_numbers_with_words(txt):
    return re.sub(r'\b\d+\b', number_to_thai_words, txt)

def _process_syllable(syllable, lao=False):
    modified_syllable = syllable

    # 1. Immediate Exceptions Check
    for exception, replacement in proprietary_exceptions.items():
        if modified_syllable == exception: return replacement
    for exception, replacement in exact_exceptions.items():
        if modified_syllable == exception: return replacement
    for exception, replacement in compounds.items():
        if modified_syllable == exception: return replacement

    for exception, replacement in karan_combinations.items():
        if modified_syllable.endswith(exception):
            modified_syllable = modified_syllable.replace(exception, replacement)

    # 2. Lao-to-Thai Crossover Scripts Processing
    if lao:
        if modified_syllable.startswith('ย'):
            modified_syllable = '\ue015' + modified_syllable[1:]
        if modified_syllable.endswith('ย'):
            modified_syllable = modified_syllable[:-1] + 'ย'
        if 'ช' in modified_syllable:
            modified_syllable = modified_syllable.replace('ช', 'ຊ')
        if 'ร' in modified_syllable:
            modified_syllable = modified_syllable.replace('ร', 'ฮ')

    # 3. Main Regex Vowel Engine Matcher
    shape_check = re.sub(r'[่้๊๋็์]', '', modified_syllable)

    for pattern, replacement in vowel_formats.items():
        escaped_pattern = re.escape(pattern)
        vowels_to_avoid = "ะาิีึືุูเแโົໍັຳຽ"
        regex_pattern = f"^{escaped_pattern.replace('\\-', '([ก-ฮ\\ue000-\\ue013ชຮ]+)').replace('_', '([ก-ฮ\\ue000-\\ue013ชຮ]+)')}(?![{vowels_to_avoid}])$"
        match = re.match(regex_pattern, shape_check)

        if match:
            groups = match.groups()
            initial_thai = groups[0] if len(groups) > 0 else ""
            final_thai = groups[1] if len(groups) > 1 else ""

            if ('ว' in pattern or 'ว' in pattern) and (initial_thai.endswith('ว') or initial_thai.endswith('ว')):
                continue

            # --- 1. Clean Silent Prefixes ('อ' นำ and 'ห' นำ) ---
            if initial_thai == 'อ':
                initial_thai = ""
            elif len(initial_thai) > 1 and initial_thai.startswith('อ'):
                initial_thai = initial_thai[1:]  # e.g., อย -> ย

            # --- 2. Cluster Analysis & initial_latin Generation ---
            true_clusters = {'กร', 'กล', 'กว', 'ขร', 'ขล', 'ขว', 'คร', 'คล', 'คว',
                             'ตร', 'ปร', 'ปล', 'ผล', 'ผว', 'พร', 'พล', 'บร', 'บล',
                             'ฟร', 'ฟล', 'ดร'}
            fake_clusters = {'จร', 'ซร', 'ศร', 'สร'}

            # NEW INTERCEPT: If it's a 'ห นำ' word, strip the ห and skip cluster checks entirely!
            if len(initial_thai) > 1 and initial_thai.startswith('ห'):
                initial_thai = initial_thai[1:]  # strip the ห
                initial_latin = "".join([thai_transliteration.get(c, c) for c in initial_thai])

            elif len(initial_thai) == 2:
                if initial_thai == 'ทร':
                    initial_latin = 's'  # ทร makes an 's' sound (e.g., ทราบ)
                elif initial_thai in fake_clusters:
                    initial_latin = thai_transliteration.get(initial_thai[0], initial_thai[0])
                elif initial_thai in true_clusters:
                    initial_latin = "".join([thai_transliteration.get(c, c) for c in initial_thai])
                else:
                    char1 = thai_transliteration.get(initial_thai[0], initial_thai[0])
                    char2 = thai_transliteration.get(initial_thai[1], initial_thai[1])
                    initial_latin = f"{char1}a{char2}"
            else:
                initial_latin = "".join([thai_transliteration.get(c, c) for c in initial_thai])

            # --- 3. Build final_latin with mae_ rules ---
            final_latin_chars = []
            for c in final_thai:
                if c in mae_kok:
                    final_latin_chars.append('k')
                elif c in mae_kon:
                    final_latin_chars.append('r' if 'คร' in initial_thai and c == 'ร' else 'n')
                elif c in mae_kod:
                    final_latin_chars.append('d')
                elif c in mae_kot:
                    final_latin_chars.append('t')
                else:
                    final_latin_chars.append(thai_transliteration.get(c, c))

            final_latin = "".join(final_latin_chars)

            return replacement.replace('-', initial_latin).replace('_', final_latin)

    # 4. Fallback Processing Block (Runs only if no vowel formats matched above)
    for exception, replacement in exceptions.items():
        modified_syllable = modified_syllable.replace(exception, replacement)

    # Handle Ro Han (รร)
    if 'รร' in modified_syllable:
        if len(shape_check) == 3:
            modified_syllable = modified_syllable.replace('รร', 'an')
        else:
            modified_syllable = modified_syllable.replace('รร', 'a')

    # Special word exceptions ending in 'ร' (The "orn" sounds)
    orn_defaults = {
        "กร": "korn", "ขร": "khorn", "คร": "khorn", "ตร": "torn",
        "จร": "jorn", "พร": "phorn", "ภร": "phorn", "สร": "sorn", "ศร": "sorn",
        "ทร": "thorn"
    }
    if shape_check in orn_defaults:
        return orn_defaults[shape_check]

    # Map general final consonants to clean baseline characters
    if modified_syllable:
        if modified_syllable[-1] in mae_kok:
            modified_syllable = modified_syllable[:-1] + 'ก'
        elif modified_syllable[-1] in mae_kon and 'คร' not in modified_syllable:
            modified_syllable = modified_syllable[:-1] + 'น'
        elif modified_syllable[-1] in mae_kod:
            modified_syllable = modified_syllable[:-1] + 'ด'
        elif modified_syllable[-1] in mae_kot:
            modified_syllable = modified_syllable[:-1] + 't'

    # Handle 2-Consonant Implied Vowels (e.g., พบ -> phop, มด -> mot)
    if len(shape_check) == 2 and all(c in thai_consonants for c in shape_check):
        if shape_check.endswith('ว'):
            modified_syllable = thai_transliteration.get(shape_check[0], '') + 'ua'
        else:
            modified_syllable = shape_check[0] + 'o' + shape_check[1]

    # Handle 3-Consonant Khmer Loans / Implied Vowels (e.g., สบถ -> sabot)
    elif len(shape_check) == 3 and all(c in valid_khmer_loans for c in shape_check):
        modified_syllable = f"{shape_check[0]}a{shape_check[1]}o{shape_check[2]}"

    for exception, replacement in ro_rue_lo_lue.items():
        if exception in modified_syllable:
            modified_syllable = modified_syllable.replace(exception, replacement)

    # 5. Final Character Mapping Pass
    transliterated_syllable = ''
    for char in modified_syllable:
        transliterated_syllable += thai_transliteration.get(char, char)

    return transliterated_syllable.strip()


def thai_words(text, number_style='keep'):
    text_processed = maiyamok(text)
    text_processed = pythainlp.tokenize.word_detokenize(text_processed)

    if number_style == 'words':
        text_processed = replace_numbers_with_words(text_processed)

    sentences = pythainlp.tokenize.sent_tokenize(text_processed, engine="crfcut")
    transliterated_sentences = []

    for sentence in sentences:
        words = pythainlp.tokenize.word_tokenize(sentence, engine='newmm')
        transliterated_words = []

        for word in words:
            if word.isspace():
                transliterated_words.append(word)
                continue
            for exception, replacement in preproprietary_exceptions.items():
                word = word.replace(exception, replacement)

            temp_syllables = pythainlp.tokenize.syllable_tokenize(word)
            syllable_transliterated_text = "".join([_process_syllable(s) for s in temp_syllables])
            transliterated_words.append(syllable_transliterated_text)

        transliterated_sentence = " ".join(transliterated_words)
        transliterated_sentence = re.sub(r' +', ' ', transliterated_sentence)
        transliterated_sentences.append(transliterated_sentence.strip())

    return " · ".join(transliterated_sentences)

def thai_syllables(text, number_style='keep'):
    lines = text.split('\n')
    transliterated_lines = []

    for line in lines:
        if not line.strip():
            transliterated_lines.append('')
            continue

        text_processed = maiyamok(line)
        text_processed = pythainlp.tokenize.word_detokenize(text_processed)
        if number_style == 'words':
            text_processed = replace_numbers_with_words(text_processed)

        for exception, replacement in preproprietary_exceptions.items():
            text_processed = text_processed.replace(exception, replacement)

        sentences = pythainlp.tokenize.sent_tokenize(text_processed, engine="crfcut")
        transliterated_sentences = []

        for sentence in sentences:
            syllables = pythainlp.tokenize.syllable_tokenize(sentence, engine="han_solo")
            transliterated_syllables = [_process_syllable(s, lao=False) for s in syllables]
            transliterated_sentence = ' '.join(transliterated_syllables)
            transliterated_sentences.append(re.sub(r' +', ' ', transliterated_sentence).strip())

        transliterated_lines.append(' · '.join(transliterated_sentences))

    return '\n'.join(transliterated_lines)

def lao_fix(text, number_style='keep'):
    lines = text.split('\n')
    transliterated_lines = []

    for line in lines:
        if not line.strip():
            transliterated_lines.append('')
            continue

        text_processed = maiyamok(line)
        text_processed = pythainlp.tokenize.word_detokenize(text_processed)
        if number_style == 'words':
            text_processed = replace_numbers_with_words(text_processed)

        for exception, replacement in preproprietary_exceptions.items():
            text_processed = text_processed.replace(exception, replacement)

        sentences = pythainlp.tokenize.sent_tokenize(text_processed, engine="crfcut")
        transliterated_sentences = []

        for sentence in sentences:
            syllables = pythainlp.tokenize.syllable_tokenize(sentence, engine="han_solo")
            transliterated_syllables = [_process_syllable(s, lao=True) for s in syllables]
            transliterated_sentence = ' '.join(transliterated_syllables)
            transliterated_sentences.append(re.sub(r' +', ' ', transliterated_sentence).strip())

        transliterated_lines.append(' · '.join(transliterated_sentences))

    return '\n'.join(transliterated_lines)