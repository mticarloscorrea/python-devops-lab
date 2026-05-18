"""Word service."""
def build_word(words):
    """Build word from list."""
    result = ""

    for index, word in enumerate(words):
        result += word[index]

    return result
