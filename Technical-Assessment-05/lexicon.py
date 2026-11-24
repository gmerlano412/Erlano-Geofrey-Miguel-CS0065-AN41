import re
from pathlib import Path

folder = Path(__file__).parent / "data"


def load(filename):
    lines = (folder / filename).read_text(encoding="latin-1").splitlines()
    return {line.strip().lower() for line in lines
            if line.strip() and not line.startswith(";")}


happy_words = load("positive-words.txt")
sad_words = load("negative-words.txt")

sentence = input("Enter a sentence: ").lower()
words = [w.strip("-'") for w in re.findall(r"[a-z0-9'+-]+", sentence)]

happy = sum(w in happy_words for w in words)
sad = sum(w in sad_words for w in words)

print("Happy words:", happy)
print("Sad words:", sad)

if happy > sad:
    print("Positive")
elif sad > happy:
    print("Negative")
else:
    print("Neutral")
