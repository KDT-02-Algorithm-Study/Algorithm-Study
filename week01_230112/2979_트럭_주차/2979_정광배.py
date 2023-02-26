# 2979 트럭 주차

a, b, c = map(int, input().split())
data = [0] * 101
for _ in range(3):
    i, o = map(int, input().split())
    for n in range(i, o):
        data[n] += 1
result = 0
result += data.count(1) * a
result += data.count(2) * b * 2
result += data.count(3) * c * 3
print(result)