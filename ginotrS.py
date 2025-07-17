s = input().strip()

lowercase = []
uppercase = []
digits_odd = []
digits_even = []

for char in s:
    if char.islower():
        lowercase.append(char)
    elif char.isupper():
        uppercase.append(char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            digits_odd.append(char)
        else:
            digits_even.append(char)

lowercase_sorted = sorted(lowercase)
uppercase_sorted = sorted(uppercase)
digits_odd_sorted = sorted(digits_odd)
digits_even_sorted = sorted(digits_even)

result = ''.join(lowercase_sorted) + ''.join(uppercase_sorted) + ''.join(digits_odd_sorted) + ''.join(digits_even_sorted)
print(result)
