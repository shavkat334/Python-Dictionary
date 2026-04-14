def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result = {}
    for index, num in enumerate(numbers):
        if num not in result:
            result[num] = []
        result[num].append(index)
    return result

# Tekshirish: 
print(group_indices([1, 2, 1, 3, 2, 1]))