def most_common_char(text: str) -> str:
    counts = {}
    for char in text:
        if char != " ":
            counts[char] = counts.get(char, 0) + 1
    return max(counts, key=counts.get)

print(most_common_char("python dictionary exercises"))