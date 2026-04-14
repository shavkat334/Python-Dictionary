def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    # Qiymati 0 ga teng bo'lmaganlarini yangi lug'atga yig'amiz
    return {key: value for key, value in d.items() if value != 0}

print(filter_non_zero({'a': 5, 'b': 0, 'c': -1, 'd': 0}))