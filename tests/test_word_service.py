from app.services.word_service import build_word


def test_build_word():
    words = ["yoda", "best", "has"]

    result = build_word(words)

    assert result == "yes"


def test_build_word_with_other_values():
    words = ["cat", "dog", "sun"]

    result = build_word(words)

    assert result == "con"