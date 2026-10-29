my_tuple = ("apple", 10, 2.5, "banana", 7, 3.14, "orange")

strings = [el for el in my_tuple if isinstance(el, str)]

print(strings)
