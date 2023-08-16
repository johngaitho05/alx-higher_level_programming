#!/usr/bin/python3
def roman_to_int(roman_string):
    _map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string or any(c not in _map for c in roman_string):
        return 0
    count = 1
    letter = roman_string[0]
    for i in range(1, len(roman_string)):
        new_letter = roman_string[i]
        if _map[new_letter] > _map[letter] and count > 1:
            return 0
        if new_letter != letter:
            count = 1
        else:
            count += 1
        letter = new_letter
    res, i, length = 0, 0, len(roman_string) - 1
    while i <= length:
        current = _map[roman_string[i]]
        _next = _map[roman_string[i + 1]] if i < length else None
        if _next and _next > current:
            current = _next - current
            i += 1
        res += current
        i += 1

    return res

