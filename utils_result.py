import os
from datetime import datetime

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_log(path, content):
    with open(path, "a", encoding="utf-8") as f:
        f.write(content + "\n")

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")