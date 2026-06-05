def transliterate_burmese(text):
    burmese_transliteration = {
        'က': 'k', 'ခ': 'kh', 'ဂ': 'g', 'ဃ': 'gh', 'င': 'ng', 'စ': 'c', 'ဆ': 'ss', 'ဇ': 'z', 'ဈ': 'zh',
        'ဉ': 'ny', 'ည': 'ny', 'ဋ': 't', 'ဌ': 'ht', 'ဍ': 'd', 'ဎ': 'd', 'ဏ': 'n', 'တ': 't', 'ထ': 'ht',
        'ဒ': 'd', 'ဓ': 'dh', 'န': 'n', 'ပ': 'p', 'ဖ': 'ph', 'ဗ': 'b', 'ဘ': 'bh', 'မ': 'm', 'ယ': 'y',
        'ရ': 'r', 'လ': 'l', 'ဝ': 'w', 'သ': 's', 'ဟ': 'h', 'ဠ': 'la', 'အ': 'a', 'ဣ': 'i', 'ဤ': 'ī',
        'ဥ': 'u', 'ဦ': 'ū', 'ဧ': 'e', 'ဩ': 'o', 'ဪ': 'au', 'ါ': 'a', 'ာ': 'ar', 'ိ': 'i',
        'ီ': 'ī', 'ု': 'u', 'ူ': 'ū', 'ေ': 'e', 'ဲ': 'e', 'ံ': 'an', '့': 'n', 'း': 'r', '္': '', '်': '',
        'ျ': 'ya', 'ြ': 'ya', 'ွ': 'wa', 'ှ': 'ha', 'ဿ': 'sa', '၍': 'yui', '၌': 'nai', '၀': '0',
        '၁': '1', '၂': '2', '၃': '3', '၄': '4', '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9',
        '၊': ',', '။': '.',
    }

    combinations = {
        '၏': '-eat',
        '၎င်း': 'lakaung',
        '၎': 'lakaung',
        'အို': 'o',
        'ုံး': 'one',
        'ုံ': 'one',
        'ိုင်': 'ine',
        'င့': 'ng',
        'ို': 'o',
        'ြစ်': 'yit',
        'ည်': 'ai',

    }

    for comb, repl in combinations.items():
        text = text.replace(comb, repl)

    transliterated_text = text
    for bucy, latin in burmese_transliteration.items():
        transliterated_text = transliterated_text.replace(bucy, latin)

    return transliterated_text