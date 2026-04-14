def count_letters(text: str) -> dict[str, int]:
    result = {}
    for char in text:
        # Bo'sh joylarni hisobga olmaymiz
        if char != " ":
            result[char] = result.get(char, 0) + 1
    return result

print(count_letters("assalomu alaykum"))