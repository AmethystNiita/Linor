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
    'อ': 'o', 'ฮ': 'h', 'ะ': 'a', 'ั': 'a', 'า': 'ā', 'ิ': 'i',
    'ี': 'ī', 'ึ': 'ue', 'ื': 'ue', 'ุ': 'u', 'ู': 'ū', 'เ': 'ē',
    'แ': 'æ', 'โ': 'ō', 'ใ': 'ai', 'ไ': 'ai', 'ำ': 'am', '่': '',
    '้': '', '๊': '', '๋': '', '๋': '', '็': '', '์': '', 'ๆ': '', 'ํ': 'ang',
    'ฤ': 'rue', 'ฦ': 'lue',
    '\ue000': 'kr', '\ue001': 'khr', '\ue002': 'tr', '\ue003': 'pr',
    '\ue004': 'phr', '\ue005': 'kl', '\ue006': 'khl', '\ue007': 'pl',
    '\ue008': 'phl', '\ue009': 'kw', '\ue010': 'khw', '\ue011': 'sr',
    '\ue012': 's', '\ue013': 'w', '\ue014': ''
}

thai_consonants = (
    'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ',
    'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ล', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'ฮ', 'ฤ')

valid_khmer_loans = (
    'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ',
    'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'ฮ')

mae_kok = {'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ'}
mae_kon = {'น', 'ร', 'ญ', 'ณ', 'ฬ'}
mae_kod = {'จ', 'ช', 'ซ', 'ฎ', 'ด', 'ศ', 'ษ', 'ส'}
mae_kot = {'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ต', 'ถ', 'ท', 'ธ'}
mae_koei = {'ย'}
back_saraa = {'ไ', 'ใ', 'เ', 'แ', 'โ'}
thai_vowels = {'ะ', 'ั', 'า', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู', 'เ', 'แ', 'โ', 'ใ', 'ไ', 'ำ', '่', '้', '๊', '๋', '็',
               '์', 'ๆ'}
thai_vowels_ai_sounds = {'ไ', 'ใ'}
thai_vowels_with_no_ai_sounds = {'ะ', 'ั', 'า', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู', 'เ', 'แ', 'โ', 'ำ', '่', '้', '๊', '๋', '็',
               '์', 'ๆ'}
thai_vowels_with_no_back_saraa = {'ะ', 'ั', 'า', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู', 'ำ', '่', '้', '๊', '๋', '็', '์',
                                  'ๆ'}
karan_combinations = {
    "กดิ์": "ก", "กดิ": "ก",
    "ทธิ์": "ท", "ทธิ": "ทิ",
    "นธุ์": "น", "นธ์": "น",
    "ภูมิ": "พูม", "ภูมิ์": "พูม",
    "รษฐ์": "d", "รษฐ": "dta", "ตน์": "ต", "สตร์": "ต", "ทย์": "ต",
    "รติ": "t", "ศน์": "ต", "ตริย์": "t",
    "าธิ": "āt", "าติ": "āt", "ัติ": "at",
    "กษณ์": "k",
    "นต์": "น", "นตร์": "น",
    "รณ์": 'orn',
    "งค์": "ง",
    "ทร์": "",

    "ก์": "", "ข์": "", "ค์": "", "ฆ์": "", "ง์": "",
    "จ์": "", "ฉ์": "", "ช์": "", "ซ์": "", "ฌ์": "", "ญ์": "",
    "ฎ์": "", "ฏ์": "", "ฐ์": "", "ฑ์": "", "ฒ์": "", "ณ์": "",
    "ด์": "", "ต์": "", "ถ์": "", "ท์": "", "ธ์": "", "น์": "",
    "บ์": "", "ป์": "", "ผ์": "", "ฝ์": "", "พ์": "", "ฟ์": "",
    "ภ์": "", "ม์": "", "ย์": "", "ร์": "r", "ล์": "", "ว์": "",
    "ษ์": "", "ส์": ""
}

# Invisible Unicode characters for the code to treat it as one character for each consonant cluster
combo_consonants = {'\ue000', '\ue001', '\ue002', '\ue003', '\ue004', '\ue005', '\ue006', '\ue007', '\ue008',
                    '\ue009', '\ue010', '\ue011', '\ue012', '\ue013'}

# Rue and Lue letter combinations
ro_rue_lo_lue = {
    'ฤๅ': 'rue',
    'ฦๅ': 'lue',
    'กฤ': 'kri',
    'ตฤ': 'tari',
    'ทฤ': 'thari',
    'ปฤ': 'pari',
    'ศฤ': 'sri',
    'สฤ': 'sri',
    'คฤ': 'karue',
    'นฤ': 'narue',
    'พฤ': 'pharue',
    'มฤ': 'marue',
    'หฤ': 'harue'
}

# Replacements
exceptions = {
    '่': '',
    '้': '',
    '๊': '',
    '๋': '',
    'ัว': 'ua',
    'ฯลฯ': 'lae uen uen',
}

# Interesting exceptions
exact_exceptions = {
    'ลออ': 'la or',
    'บ่': 'bo',
    'ก็': 'ko'
}

# Abbreviations
preproprietary_exceptions = {
    'ค.ศ.': 'khristsakarād',
    'พ.ศ.': 'phuthasakarād'
}

# Whole words
proprietary_exceptions = {
    'เสมอ': 'samœ',
    'เสนอ': 'sanœ',
    'เพราะ': 'phro',
    'เฉพาะ': 'chapor',
    'ไหม์': 'haim',
    'อย่า': 'yā',
    'อยู่': 'yū',
    'อย่าง': 'yāng',
    'อยาก': 'yāk',
    'โทรศัพท์': 'tōra sap',
    'เสมือน': 'sameuan',
    'โทร': 'tō',
    'เหว': 'hēw',
    'หวง': 'huang',
    'หงส์': 'hong',
    'บรม': 'borom',
    'นคร': 'nakhorn',
    'วิศว': 'witsawa',
    'วิศวะ': 'witsawa',
    'เสน่ห์': 'sanē',
    'เสนาะ': 'sanor'
}

# Compounds / Parts of compounds
compounds = {
    'บาร': 'bāra',
    'พุทธ': "phutha"
}

# Letter swaps and stuff
post_exceptions = {
    'ēueo': 'eua',
    'ēā': 'ao',
    'ēi': 'œ',
    'ēo': 'œ',
    'ēīi': 'ia',
    'ēīy': 'ia',
    'ēa': 'e',
    'aoa': 'or',
    'iaua': 'ieow',
    'oo': 'or',
    'ēy': 'œi',
    'aā': 'ā',
    'iai': 'ia',
    'ii': 'ai',
    'aa': 'a',
    'āa': 'ā',
    '. ..': '...',
    ' ,': ','
}

def number_to_thai_words(match):
    number = int(match.group())
    return num2words(number, lang='th')

def replace_numbers_with_words(txt):
    return re.sub(r'\b\d+\b', number_to_thai_words, txt)

def _process_syllable(syllable):
    # Variable set
    modified_syllable = syllable

    # Apply proprietary and exact exceptions
    for exception, replacement in proprietary_exceptions.items():
        if modified_syllable == exception:
            return replacement
    for exception, replacement in exact_exceptions.items():
        if modified_syllable == exception:
            return replacement
    for exception, replacement in compounds.items():
        if modified_syllable == exception:
            return replacement

    # Karan combinations
    for exception, replacement in karan_combinations.items():
        if modified_syllable.endswith(exception):
            if modified_syllable == exception:
                pass
            else:
                modified_syllable = modified_syllable.replace(exception, replacement)

    # Normal exceptions
    for exception, replacement in exceptions.items():
        modified_syllable = modified_syllable.replace(exception, replacement)

    # Ro han
    if 'รร' in modified_syllable:
        if len(modified_syllable) == 3:
            modified_syllable = modified_syllable.replace('รร', 'an')
        if len(modified_syllable) == 4:
            modified_syllable = modified_syllable.replace('รร', 'a')

    # Bad unoptimized detection for consonant clusters
    if "กร" in modified_syllable or "ขร" in modified_syllable or "คร" in modified_syllable:
        if modified_syllable == "กร":
            modified_syllable = modified_syllable.replace("กร", "korn")
        elif modified_syllable == "ขร":
            modified_syllable = modified_syllable.replace("ขร", "khorn")
        elif (modified_syllable ==
              "คร"):
            modified_syllable = modified_syllable.replace("คร", "khorn")
        elif "กร" in modified_syllable:
            modified_syllable = modified_syllable.replace('กร', '\ue000')
        elif "ขร" in modified_syllable:
            modified_syllable = modified_syllable.replace('ขร', '\ue001')
        elif "คร" in modified_syllable:
            modified_syllable = modified_syllable.replace('คร', '\ue001')
    if modified_syllable == "กล":
        modified_syllable = modified_syllable.replace("กล", "kon")
    elif modified_syllable == "ขล":
        modified_syllable = modified_syllable.replace("ขล", "khon")
    elif modified_syllable == "คล":
        modified_syllable = modified_syllable.replace("คล", "khon")
    elif "กล" in modified_syllable:
        modified_syllable = modified_syllable.replace('กล', '\ue005')
    elif "ขล" in modified_syllable:
        modified_syllable = modified_syllable.replace('ขล', '\ue006')
    elif "คล" in modified_syllable:
        modified_syllable = modified_syllable.replace('คล', '\ue006')
    if "กล" in modified_syllable or "ขล" in modified_syllable or "คล" in modified_syllable:
        pass
    if "นร" in modified_syllable:
        if modified_syllable == "นร":
            modified_syllable = "nora"
        elif modified_syllable == "นรา":
            modified_syllable = "narā"
    if "ปร" in modified_syllable:
        if modified_syllable == "ปร":
            modified_syllable = "pora"
        elif "ปร" in modified_syllable:
            modified_syllable = modified_syllable.replace('ปร', '\ue003')
    if "ปล" in modified_syllable:
        modified_syllable = modified_syllable.replace('ปล', '\ue007')
    if "พร" in modified_syllable:
        if modified_syllable == "พร":
            modified_syllable = "phorn"
        elif "พร" in modified_syllable:
            modified_syllable = modified_syllable.replace('พร', '\ue004')
    if "ภร" in modified_syllable:
        if modified_syllable == "ภร":
            modified_syllable = "phorn"
    if "พล" in modified_syllable:
        if modified_syllable == "พล":
            modified_syllable = "pol"
        elif "พล" in modified_syllable:
            modified_syllable = modified_syllable.replace('พล', '\ue008')
    if "ตร" in modified_syllable:
        if modified_syllable == "ตร":
            modified_syllable = "torn"
        elif "ตร" in modified_syllable:
            modified_syllable = modified_syllable.replace('ตร', '\ue002')
    if "จร" in modified_syllable:
        if modified_syllable == "จร":
            modified_syllable = "jorn"
        elif "จร" in modified_syllable:
            modified_syllable = modified_syllable.replace('จร', 'จ')
    if "รถ" in modified_syllable:
        if modified_syllable == "รถ":
            modified_syllable = "rod"
        elif "รถ" in modified_syllable:
            modified_syllable = modified_syllable.replace('รถ', 'rd')
    if "สร" in modified_syllable or "ศร" in modified_syllable:
        if modified_syllable == "สร" or modified_syllable == "ศร":
            modified_syllable = "sorn"
        elif "สร" in modified_syllable:
            modified_syllable = modified_syllable.replace('สร', '\ue011')
        elif "ศร" in modified_syllable:
            modified_syllable = modified_syllable.replace('ศร', '\ue011')
    if "ทร" in modified_syllable:
        if modified_syllable == "ทร":
            modified_syllable = "thorn"
        elif "ทร" in modified_syllable:
            modified_syllable = modified_syllable.replace('ทร', '\ue012')
    if "ห" in modified_syllable:
        if modified_syllable == "หน":
            modified_syllable = "hon"
        elif modified_syllable == "หม":
            modified_syllable = "hom"
        elif modified_syllable == "หร":
            modified_syllable = "hor"
        elif "หง" in modified_syllable:
            modified_syllable = modified_syllable.replace('หง', 'ง')
        elif "หญ" in modified_syllable:
            modified_syllable = modified_syllable.replace('หญ', 'ญ')
        elif "หน" in modified_syllable:
            modified_syllable = modified_syllable.replace('หน', 'น')
        elif "หม" in modified_syllable:
            modified_syllable = modified_syllable.replace('หม', 'ม')
        elif "หย" in modified_syllable:
            modified_syllable = modified_syllable.replace('หย', 'ย')
        elif "หร" in modified_syllable:
            modified_syllable = modified_syllable.replace('หร', 'ร')
        elif "หล" in modified_syllable:
            modified_syllable = modified_syllable.replace('หล', 'ล')

        hw_vowel_flag = False
        if "หว" in modified_syllable:
            for vowel in thai_vowels:
                if vowel in modified_syllable:
                    hw_vowel_flag = True
            if hw_vowel_flag == True:
                if 'หว' in modified_syllable:
                    modified_syllable = modified_syllable.replace('หว', '\ue013')

    kw_vowel_flag = False
    if 'กว' in modified_syllable or 'ขว' in modified_syllable or 'คว' in modified_syllable:
        for vowel in thai_vowels:
            if vowel in modified_syllable:
                kw_vowel_flag = True
        if kw_vowel_flag == True:
            if 'กว' in modified_syllable:
                modified_syllable = modified_syllable.replace('กว', '\ue009')
            elif 'ขว' in modified_syllable:
                modified_syllable = modified_syllable.replace('ขว', '\ue010')
            elif 'คว' in modified_syllable:
                modified_syllable = modified_syllable.replace('คว', '\ue010')

    # Vowels with Yo Yak
    if modified_syllable.endswith('อย'):
        modified_syllable = modified_syllable.replace('อย', 'oi')
    elif modified_syllable.endswith('วย'):
        modified_syllable = modified_syllable.replace('วย', 'uai')

    # Ro Rue and Lo Lue
    for exception, replacement in ro_rue_lo_lue.items():
        if exception in modified_syllable:
            modified_syllable = modified_syllable.replace(exception, replacement)

    # Reorder vowels
    for i, char in enumerate(syllable):
        if char in back_saraa and i < len(syllable) - 1:
            modified_syllable = modified_syllable[:i] + modified_syllable[i + 1] + char + modified_syllable[
                i + 2:]

    # Handle final consonants
    if modified_syllable and modified_syllable[-1] in mae_kok:
        modified_syllable = modified_syllable[:-1] + 'ก'
    elif modified_syllable and modified_syllable[-1] in mae_kon:
        if 'คร' in modified_syllable:
            pass
        else:
            modified_syllable = modified_syllable[:-1] + 'น'
    elif modified_syllable and modified_syllable[-1] in mae_kod:
        modified_syllable = modified_syllable[:-1] + 'ด'
    elif modified_syllable and modified_syllable[-1] in mae_kot:
        modified_syllable = modified_syllable[:-1] + 't'
    elif modified_syllable and modified_syllable[-1] in mae_koei:
        for ai in thai_vowels_ai_sounds:
            if ai in modified_syllable:
                modified_syllable = modified_syllable[:-1] + ''
                break
        for saraa in thai_vowels_with_no_ai_sounds:
            if saraa in modified_syllable and modified_syllable.endswith('ย'):
                modified_syllable = modified_syllable[:-1] + 'ii'
                break

    # Handle Khmer loanword rule
    if len(modified_syllable) == 3 and all(keyword in valid_khmer_loans for keyword in modified_syllable):
        first_consonant = modified_syllable[0]
        second_consonant = modified_syllable[1]
        third_consonant = modified_syllable[2]
        modified_syllable = f"{first_consonant}a{second_consonant}o{third_consonant}"

    # Exception for words with Wo Waen in the middle
    i = 0
    while i < len(modified_syllable) - 1 and len(modified_syllable) != 2:
        char = modified_syllable[i]
        next_char = modified_syllable[i + 1]
        if modified_syllable.endswith('ว') and modified_syllable[-2] in thai_vowels:
            modified_syllable = modified_syllable.replace('ว', 'o')
            break
        elif char in thai_consonants and next_char == 'ว':
            modified_syllable = modified_syllable.replace('ว', 'ua')
        elif char in combo_consonants and next_char == 'ว':
            modified_syllable = modified_syllable.replace('ว', 'ua')
        elif char in thai_consonants and next_char in thai_consonants:
            modified_syllable = modified_syllable[:i + 1] + 'a' + modified_syllable[i + 1:]
            i += 2
        elif char == 'อ' and next_char in thai_vowels:
            modified_syllable = modified_syllable.replace('อ', '')
        else:
            i += 1

    # Exception for words with Or Ang
    while len(modified_syllable) == 2:
        modified_syllable += "\ue014"
        char = modified_syllable[i]
        next_char = modified_syllable[i + 1]
        if char in thai_consonants and next_char in thai_consonants:
            modified_syllable = modified_syllable[:i + 1] + 'o' + modified_syllable[i + 1:]
            i += 2
        elif char in combo_consonants and next_char in thai_consonants:
            modified_syllable = modified_syllable[:i + 1] + 'o' + modified_syllable[i + 1:]
            i += 2
        elif char == 'อ' and next_char in thai_vowels:
            modified_syllable = modified_syllable.replace('อ', '')
        else:
            i += 1

    # Apply the transliteration mapping
    transliterated_syllable = ''
    for char in modified_syllable:
        transliterated_char = thai_transliteration.get(char, char)
        transliterated_syllable += transliterated_char

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
        last_transliterated_word = ""

        for word_index, word in enumerate(words):
            if word.isspace():
                transliterated_words.append(word)
                continue
            # Apply preproprietary exceptions to the word before syllabification
            for exception, replacement in preproprietary_exceptions.items():
                word = word.replace(exception, replacement)

            temp_syllables = pythainlp.tokenize.syllable_tokenize(word)
            syllable_transliterated_text = ""
            for syllable in temp_syllables:
                syllable_transliterated_text += _process_syllable(syllable)

            transliterated_words.append(syllable_transliterated_text)
            last_transliterated_word = syllable_transliterated_text

        transliterated_sentence = " ".join(transliterated_words)
        transliterated_sentence = re.sub(r' +', ' ', transliterated_sentence)

        for exception, replacement in post_exceptions.items():
            transliterated_sentence = transliterated_sentence.replace(exception, replacement)

        transliterated_sentences.append(transliterated_sentence.strip())

    transliterated_text = " · ".join(transliterated_sentences)
    transliterated_text = re.sub(r'[ \t]+', ' ', transliterated_text)
    return transliterated_text

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
            transliterated_syllables = [_process_syllable(s) for s in syllables]

            transliterated_sentence = ' '.join(transliterated_syllables)
            transliterated_sentence = re.sub(r' +', ' ', transliterated_sentence)

            for exception, replacement in post_exceptions.items():
                transliterated_sentence = transliterated_sentence.replace(exception, replacement)

            transliterated_sentences.append(transliterated_sentence.strip())

        transliterated_lines.append(' · '.join(transliterated_sentences))

    return '\n'.join(transliterated_lines)

# print(thai_words("อิสริยาภรณ์"))
# print(thai_syllables("อิสริยาภรณ์"))