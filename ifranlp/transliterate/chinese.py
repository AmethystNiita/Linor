from pypinyin import pinyin, Style

def transliterate_chinese(text):
    punctuation = {
        '，': ',',
        '、': ',',
        '。': '.',
        '（': '(',
        '）': ')',
        '？': '?',
        '！': '!'
    }

    manipulation = {
        ' ,': ',',
        ' .': '.',
        ' ?': '?',
        ' !': '!',
        '\n ': '\n'
    }

    if not text:
        return ""

    for exception, replacement in punctuation.items():
        text = text.replace(exception, replacement)

    pinyin_list = pinyin(
        text,
        style=Style.TONE,
        heteronym=True,
    )

    output = " ".join([item[0] for item in pinyin_list])

    for exception, replacement in manipulation.items():
        output = output.replace(exception, replacement)

    return output