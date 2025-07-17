def swap_case(s):
    swapped = []
    for char in s:
        if char.isupper():
            swapped.append(char.lower())
        elif char.islower():
            swapped.append(char.upper())
        else:
            swapped.append(char)
    return ''.join(swapped)
