n, m = map(int, input().split())
lists = []
for _ in range(n):
    elements = list(map(int, input().split()))
    k = elements[0]
    current_list = elements[1:]
    lists.append(current_list)
from itertools import product
max_mod = 0
for combination in product(*lists):
    total = sum(x ** 2 for x in combination)
    current_mod = total % m
    if current_mod > max_mod:
        max_mod = current_mod
    if max_mod == m - 1:  
        break
print(max_mod)
