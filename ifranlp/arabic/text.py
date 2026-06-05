import random

tashkeel = {
    'َ', 'ِ', 'ُ',
    'ً', 'ٍ', 'ٌ',
    'ْ', 'ّ'
}

random_tashkeel = {
    'َ', 'ِ', 'ُ',
    'ً', 'ٍ', 'ٌ',
    'ْ',
}

random_tashkeel_shaddah = {
    'َ', 'ِ', 'ُ',
    'ً', 'ٍ', 'ٌ',
    'َّ', 'ِّ', 'ُّ',
    'ًّ', 'ٍّ', 'ٌّ',
    'ْ',
}

def remove_tashkeel(text, hamza=False):
    if hamza == True:
        text = text.replace('أ', 'ا')
        text = text.replace('إ', 'ا')

    for char in tashkeel:
        text = text.replace(char, '')

    return text

def sprinkle_tashkeel(text, shaddah=False):
    words = text.split()  # split into words
    sprinkled = []


    if shaddah == True:
        for w in words:
            mark = random.choice(list(random_tashkeel_shaddah))
            sprinkled.append(w + mark)
    elif shaddah == False:
        for w in words:
            mark = random.choice(list(random_tashkeel))
            sprinkled.append(w + mark)

    return " ".join(sprinkled)