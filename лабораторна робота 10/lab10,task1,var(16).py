import re
import string
from pathlib import Path


program_directory = Path(__file__).parent
input_file = program_directory / "input.txt"

if not input_file.exists():
    raise FileNotFoundError(
        f"Файл {input_file.name} не знайдено. Створіть його поруч із програмою."
    )

with input_file.open("r", encoding="utf-8") as file:
    text = file.read()

sentence_counts = {
    "Питальні речення": text.count("?"),
    "Розповідні речення": text.count("."),
    "Окличні речення": text.count("!"),
}

capital_words = re.findall(r"\b[A-Z][A-Za-z'-]*\b", text)
punctuation_marks = [symbol for symbol in text if symbol in string.punctuation]

with (program_directory / "sentence_counts.txt").open("w", encoding="utf-8") as file:
    for sentence_type, count in sentence_counts.items():
        file.write(f"{sentence_type}: {count}\n")

with (program_directory / "capital_words.txt").open("w", encoding="utf-8") as file:
    file.write("\n".join(capital_words))

with (program_directory / "punctuation_marks.txt").open("w", encoding="utf-8") as file:
    file.write(" ".join(punctuation_marks))

print("Кількість речень:", sentence_counts)
print("Слова з великої літери:", capital_words)
print("Розділові знаки:", punctuation_marks)
