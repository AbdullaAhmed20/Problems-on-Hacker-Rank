n = int(input())
word = []

for _ in range(n):
    parts = input().split()
    cmd = parts[0]

    if cmd == "insert":
        index = int(parts[1])
        value = int(parts[2])
        word.insert(index, value)
    elif cmd == "print":
        print(word)
    elif cmd == "remove":
        value = int(parts[1])
        word.remove(value)
    elif cmd == "append":
        value = int(parts[1])
        word.append(value)
    elif cmd == "sort":
        word.sort()
    elif cmd == "pop":
        word.pop()
    elif cmd == "reverse":
        word.reverse()
