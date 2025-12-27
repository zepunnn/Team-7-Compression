from ebooklib import epub
from bs4 import BeautifulSoup

def read_epub_text(path: str) -> str:
    """
    Extract plain text content from an EPUB file.
    EPUB is a container format (ZIP), so text must be parsed from HTML.
    """
    book = epub.read_epub(path)
    texts = []

    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")
            text = soup.get_text(separator=" ")
            texts.append(text)

    return "\n".join(texts)