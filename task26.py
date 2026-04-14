def merge_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict1.copy()
    result.update(dict2)
    return result

# Tekshirish 
print(merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))