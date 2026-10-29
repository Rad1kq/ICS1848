cities =[
    "Київ",
    "Львів",
    "Одеса",
    "Харків",
    "Київ",
    "Дніпро",
    "Львів",
    "Запоріжжя",
    "Полтава",
    "Одеса",
    "Чернігів",
    "Вінниця",
]


def remove_duplicates(city_list):
    return list(dict.fromkeys(city_list))


def show_second_and_penultimate(city_list):
    if len(city_list) < 2:
        print("У списку недостатньо елементів.")
        return

    print("Друге місто:", city_list[1])
    print("Передостаннє місто:", city_list[-2])


cities = remove_duplicates(cities)
print("Список міст без повторів:", cities)
show_second_and_penultimate(cities)
