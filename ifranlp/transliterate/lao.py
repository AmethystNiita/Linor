import re
import laonlp
from ifranlp.transliterate.thainew import lao_fix

lao_tone_marks = {"່": '', "້": '', "໊": '', "໋": ''}

def yo_yak(text):
    text = re.sub(r'ເ([ກ-ຮໜໝຼ]{1,2})ຍ(?![າ-ູ])', r'เ\1ีย', text)
    return text

def yo_fueang(text):
    text = re.sub(r'ເ([ກ-ຮໜໝຼ])ຽ', r'เ\1ีย', text)
    text = re.sub(r'([ກ-ຮໜໝຼ])ຽ([ກ-ມວ])', r'เ\1ีย\2', text)
    text = re.sub(r'([ກ-ຮໜໝຼ])([່້໊໋])ຽ([ກ-ມວ])', r'เ\1ีย\3', text)
    text = text.replace('ຽ', 'ย')
    for tone, nothing in lao_tone_marks.items():
        text = text.replace(tone, nothing)
    return text

def nikhahit(text):
    text = re.sub(r'([ກ-ຮໜໝຼ]{1,2})(ໍາ)([່້໊໋]?)', r'\1\2ຳ', text)
    text = re.sub(r'([ກ-ຮໜໝຼ]{1,2})(ໍ)([່້໊໋]?)', r'\1\2ອ', text)
    #text = re.sub(r'([ກ-ຮໜໝຼ]{1,2})([່້໊໋໌]?)(ື)(?![ກ-ຮ])', r'\1\2\3ອ', text)
    text = text.replace('ໍ', '')
    return text

def transliterate_lao(lao_text, number_style='keep'):
    clean_lao = yo_yak(lao_text)
    clean_lao = yo_fueang(clean_lao)
    clean_lao = nikhahit(clean_lao)
    thai_script = laonlp.lao2thai_script(clean_lao)
    thai_script = thai_script.replace('ญ', 'ย')
    print(thai_script)
    if number_style == 'words':
        latin_output = lao_fix(thai_script, number_style='words')
    else:
        latin_output = lao_fix(thai_script)
    return latin_output

if __name__ == "__main__":
    print(transliterate_lao("""
    ປະເທດລາວ ຫຼື ຊື່ຢ່າງເປັນທາງການຄື
    """))