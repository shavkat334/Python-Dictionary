def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    result = {}
    
    for student in students:
        name = student["name"]
        group = student["group"]
        
        if group not in result:
            result[group] = []
        
        result[group].append(name)
            
    return result

# Tekshirish uchun:
talabalar = [
    {"name": "Ali", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Soli", "group": "A"},
    {"name": "Karim", "group": "B"}
]

print(group_students(talabalar))