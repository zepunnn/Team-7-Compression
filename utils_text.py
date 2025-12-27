import unicodedata

def normalize_text(text: str) -> str:
    """
    Normalize Unicode text to ASCII to ensure compatibility
    with dictionary-based compression algorithms (e.g. LZW).
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    return text