import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
for num in a:
    if num > b:
        n += math.ceil((num-b)/c)

print(n)