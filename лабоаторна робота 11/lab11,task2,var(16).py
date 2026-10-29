import json
from pathlib import Path


program_directory = Path(__file__).parent
input_file = program_directory / "sick_leave.json"
sorted_file = program_directory / "sorted_sick_leave.json"

if not input_file.exists():
    raise FileNotFoundError(
        f"Файл {input_file.name} не знайдено. Створіть його поруч із програмою."
    )

with input_file.open("r", encoding="utf-8-sig") as file:
    sick_leave = json.load(file)

sorted_sick_leave = dict(
    sorted(sick_leave.items(), key=lambda employee: employee[1], reverse=True)
)
without_sick_leave = [
    surname for surname, days in sick_leave.items() if days == 0
]
more_than_twenty_days = [
    surname for surname, days in sick_leave.items() if days > 20
]

with sorted_file.open("w", encoding="utf-8") as file:
    json.dump(sorted_sick_leave, file, ensure_ascii=False, indent=4)

print("Дані за кількістю днів у порядку спадання:")
for surname, days in sorted_sick_leave.items():
    print(f"{surname}: {days}")

print("Працівники без лікарняних:", without_sick_leave)
print("Працівники, які хворіли понад 20 днів:", more_than_twenty_days)
