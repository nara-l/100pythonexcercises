
def translator(word):
    d = dict(weather="clima", earth="terra", rain="chuva")
    try:
        return d[word.lower()]
    except KeyError:
        return "We don't understand your choice."

word = input("Please enter a word to translate, weather, earth, rain etc. \n ")

print(translator(word))
