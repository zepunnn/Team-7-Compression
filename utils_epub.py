from ebooklib import epub
from bs4 import BeautifulSoup

def read_epub_text(path: str) -> str:
    """
    Extract plain text from EPUB by parsing HTML/XHTML content.
    Compatible with various ebooklib object types.
    """
    book = epub.read_epub(path)
    texts = []

    for item in book.get_items():
        media_type = getattr(item, "media_type", None)

        if media_type in ("application/xhtml+xml", "text/html"):
            soup = BeautifulSoup(item.get_content(), "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            if text:
                texts.append(text)

    return "\n".join(texts)