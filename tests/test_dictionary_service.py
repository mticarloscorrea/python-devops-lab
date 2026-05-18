from app.services.dictionary_service import Dictionary

def test_dictionary_returns_existing_entry():
    dictionary = Dictionary()

    dictionary.newentry("Apple", "A fruit that grows on trees")

    result = dictionary.look("Apple")

    assert result == "A fruit that grows on trees"


def test_dictionary_returns_not_found_message():
    dictionary = Dictionary()

    result = dictionary.look("Banana")

    assert result == "Can't find entry for Banana"