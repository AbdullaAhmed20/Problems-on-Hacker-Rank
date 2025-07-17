n = int(input())
records = {}

for _ in range(n):
    parts = input().split()
    name = parts[0]
    scores = list(map(float, parts[1:]))
    records[name] = scores

query = input()
avg = sum(records[query]) / 3
print(f"{avg:.2f}")
