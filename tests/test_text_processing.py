def clean_text(text: str) -> str:
    return text.lower().strip()


def test_clean_text_lowercase():
    result = clean_text("HELLO WORLD")
    assert result == "hello world"


def test_clean_text_strip():
    result = clean_text("  Test  ")
    assert result == "test"
