def capitalize_all_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())


example = "wiatj swiecie"
print(capitalize_all_words(example))