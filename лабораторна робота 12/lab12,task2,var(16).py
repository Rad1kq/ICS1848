import string
from pathlib import Path


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


program_directory = Path(__file__).parent
input_file = program_directory / "story.txt"
output_file = program_directory / "all.txt"

if not input_file.exists():
    raise FileNotFoundError(
        f"Файл {input_file.name} не знайдено. Створіть його поруч із програмою."
    )

with input_file.open("r", encoding="utf-8-sig") as file:
    story = file.read()

clean_story = remove_punctuation(story)

with output_file.open("w", encoding="utf-8") as file:
    file.write(clean_story)

print(f"Текст без розділових знаків записано у файл {output_file.name}.")
