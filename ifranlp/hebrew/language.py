def smart_shva(text):
    shva_probability = {
        'לְפּ': 'lp', 'לְפ': 'lf', 'יְה': 'yeh',
        'בְּ ': 'b ', 'וְ ': 'v ', 'לְ ': 'l ', 'הְ ': 'h ', 'פְּ ': 'p ', 'גְּ ': 'g ',
        'בְּ': 'be', 'וְ': 've', 'לְ': 'le', 'הְ': 'he', 'פְּ': 'pe', 'גְּ': 'ge',
        'לְּ': 'le', 'תְּ': 'te',
        'רְר': 'rer',
        ' מְ': ' me'
    }

    for item, repl in shva_probability.items():
        text = text.replace(item, repl)

    return text