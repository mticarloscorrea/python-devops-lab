def build_word(words):
    result = ""

    for index, word in enumerate(words):
        result += word[index]

    return result