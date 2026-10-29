from pathlib import Path


program_directory = Path(__file__).parent
input_file = program_directory / "directories.txt"
work_directory = program_directory / "WORK"

if not input_file.exists():
    raise FileNotFoundError(
        f"Файл {input_file.name} не знайдено. Створіть його поруч із програмою."
    )

work_directory.mkdir(exist_ok=True)

with input_file.open("r", encoding="utf-8") as file:
    directory_names = [
        line.strip().lstrip("\ufeff") for line in file if line.strip()
    ]

for directory_name in directory_names:
    directory = work_directory / directory_name
    if directory.parent != work_directory:
        raise ValueError(
            f"Некоректна назва каталогу: {directory_name}. "
            "Використовуйте лише назви без шляхів."
        )
    directory.mkdir(exist_ok=True)

print(f"Створено каталогів: {len(directory_names)}")
