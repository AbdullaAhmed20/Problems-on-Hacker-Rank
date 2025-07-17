n = int(input())
words = []
count_dict = {}
order = []

for _ in range(n):
    word = input().strip()
    words.append(word)
    if word not in count_dict:
        count_dict[word] = 1
        order.append(word)
    else:
        count_dict[word] += 1

print(len(order))
print(' '.join(str(count_dict[word]) for word in order))
