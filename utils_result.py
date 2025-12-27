import os
from datetime import datetime


def ensure_dir(path: str):
    """
    Create directory if it does not exist.
    Used for results/text, results/image, results/video.
    """
    os.makedirs(path, exist_ok=True)


def write_log(path: str, content: str):
    """
    Append log information to a log file.
    Used for experiment execution logs.
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(content + "\n")


def write_analysis(path: str, content: str):
    """
    Write analysis report to a file.
    The file is overwritten each run to keep analysis clean.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


def timestamp() -> str:
    """
    Return current timestamp for logging.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")