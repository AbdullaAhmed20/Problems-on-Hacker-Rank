n = int(input())
for _ in range(n):
    number = input().strip()
    valid = True
    if not (number[0] == '4' or number[0] == '5' or number[0] == '6'):
        valid = False
    num_without_hyphens = number.replace('-', '')
    if len(num_without_hyphens) != 16:
        valid = False
    if not num_without_hyphens.isdigit():
        valid = False
    if '-' in number:
        parts = number.split('-')
        if len(parts) != 4 or any(len(part) != 4 for part in parts):
            valid = False
    for i in range(len(num_without_hyphens) - 3):
        if num_without_hyphens[i] == num_without_hyphens[i+1] == num_without_hyphens[i+2] == num_without_hyphens[i+3]:
            valid = False
            break
    print("Valid" if valid else "Invalid")
