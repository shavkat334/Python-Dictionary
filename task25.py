def group_by_age(people: list[dict]) -> dict[int, list[str]]:
    result = {}
    for person in people:
        age = person["age"]
        name = person["name"]
        if age not in result:
            result[age] = []
        result[age].append(name)
    return result

# Tekshirish:
odamlar = [{"name": "Ali", "age": 25}, {"name": "Vali", "age": 20}, {"name": "Sami", "age": 25}]
print(group_by_age(odamlar))