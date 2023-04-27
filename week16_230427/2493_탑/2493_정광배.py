# 2493 탑
# 146384 KB / 516 ms

n = int(input())

d = list(map(int, input().split()))
s = []
a = []
for i in range(n):
    while s:
        if d[i] < s[-1][1]:
            a.append(s[-1][0])
            break
        s.pop()
    if not s:
        a.append(0)
    s.append((i+1, d[i]))
print(' '.join(map(str, a)))
