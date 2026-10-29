import csv
import json
import random
from pathlib import Path


number_of_points = 100
program_directory = Path(__file__).parent
quadrants = {
    "I чверть": 0,
    "II чверть": 0,
    "III чверть": 0,
    "IV чверть": 0,
}
points_on_axes = 0
points = []

for _ in range(number_of_points):
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)

    if x > 0 and y > 0:
        quadrant = "I чверть"
    elif x < 0 and y > 0:
        quadrant = "II чверть"
    elif x < 0 and y < 0:
        quadrant = "III чверть"
    elif x > 0 and y < 0:
        quadrant = "IV чверть"
    else:
        quadrant = "На осі"
        points_on_axes += 1

    if quadrant in quadrants:
        quadrants[quadrant] += 1
    points.append({"x": x, "y": y, "quadrant": quadrant})

with (program_directory / "points.csv").open(
    "w", newline="", encoding="utf-8-sig"
) as file:
    writer = csv.DictWriter(file, fieldnames=["x", "y", "quadrant"])
    writer.writeheader()
    writer.writerows(points)

result = {
    "total_points": number_of_points,
    "quadrants": quadrants,
    "points_on_axes": points_on_axes,
}

with (program_directory / "result.json").open("w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

for quadrant, count in quadrants.items():
    print(f"{quadrant}: {count}")

print(f"Точки на осях: {points_on_axes}")
print("Дані збережено у файлах points.csv і result.json")
