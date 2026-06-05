def transliterate_mkhedruli(text):
    chars = {
        "ა": "a", "ბ": "b", "გ": "g", "დ": "d", "ე": "e", "ვ": "v", "ზ": "z", "თ": "t",
        "ი": "i", "კ": "k’", "ლ": "l", "მ": "m", "ნ": "n", "ო": "o", "პ": "p’", "ჟ": "zh",
        "რ": "r", "ს": "s", "ტ": "t’", "უ": "u", "ფ": "p", "ქ": "k", "ღ": "gh", "ყ": "q’",
        "შ": "sh", "ჩ": "ch", "ც": "ts", "ძ": "dz", "წ": "ts’", "ჭ": "ch’", "ხ": "kh",
        "ჯ": "j", "ჰ": "h", "ჱ": "e", "ჲ": "y", "ჳ": "wi", "ჴ": "q", "ჵ": "o",
        " ": " "
    }
    result = ""
    for char in text:
        result += chars.get(char, char)
    return result

def transliterate_asomtavruli(text):
    chars = {
        "Ⴀ": "a", "Ⴁ": "b", "Ⴂ": "g", "Ⴃ": "d", "Ⴄ": "e", "Ⴅ": "v", "Ⴆ": "z", "Ⴇ": "t",
        "Ⴈ": "i", "Ⴉ": "k’", "Ⴊ": "l", "Ⴋ": "m", "Ⴌ": "n", "Ⴍ": "o", "Ⴎ": "p’", "Ⴏ": "zh",
        "Ⴐ": "r", "Ⴑ": "s", "Ⴒ": "t’", "Ⴓ": "u", "Ⴔ": "p", "Ⴕ": "k", "Ⴖ": "gh", "Ⴗ": "q’",
        "Ⴘ": "sh", "Ⴙ": "ch", "Ⴚ": "ts", "Ⴛ": "dz", "Ⴜ": "ts’", "Ⴝ": "ch’", "Ⴞ": "kh",
        "Ⴟ": "j", "Ⴠ": "h",
        " ": " "
    }
    result = ""
    for char in text:
        result += chars.get(char, char)
    return result

def transliterate_nuskhuri(text):
    chars = {
        "ⴀ": "a", "ⴁ": "b", "ⴂ": "g", "ⴃ": "d", "ⴄ": "e", "ⴅ": "v", "ⴆ": "z", "ⴇ": "t",
        "ⴈ": "i", "ⴉ": "k’", "ⴊ": "l", "ⴋ": "m", "ⴌ": "n", "ⴍ": "o", "ⴎ": "p’", "ⴏ": "zh",
        "ⴐ": "r", "ⴑ": "s", "ⴒ": "t’", "ⴓ": "u", "ⴔ": "p", "ⴕ": "k", "ⴖ": "gh", "ⴗ": "q’",
        "ⴘ": "sh", "ⴙ": "ch", "ⴚ": "ts", "ⴛ": "dz", "ⴜ": "ts’", "ⴝ": "ch’", "ⴞ": "kh",
        "ⴟ": "j", "ⴠ": "h",
        " ": " "
    }
    result = ""
    for char in text:
        result += chars.get(char, char)
    return result