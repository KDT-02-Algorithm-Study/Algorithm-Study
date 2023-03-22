# 31256 KB / 44ms

D, K = map(int, input().split())
a = 1
b = 0
for _ in range(D-1):
    a, b = b, a + b

for i in range(1, K):
    tmp = (K-(i*a)) % b
    if tmp == 0:
        print(i)
        print((K-(i*a)) // b)
        break