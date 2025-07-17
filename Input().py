x,k = map(int, input().split())
polynomial = input().strip()
result = eval(polynomial.replace('x', str(x)))
print(result == k)
