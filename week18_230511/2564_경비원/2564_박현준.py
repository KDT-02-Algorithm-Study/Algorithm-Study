# 31256 KB / 44 ms

N, M = map(int, input().split())
num = int(input())
stores = []

def check(x1, y1, x2, y2):
    if x1 == 1:
        if x2 == 1:
            return abs(y1 - y2)
        if x2 == 2:
            return min((y1 + y2 + M), ((2 * N) + M - y1 - y2))
        if x2 == 3:
            return y1 + y2
        if x2 == 4:
            return N - y1 + y2
    if x1 == 2:
        if x2 == 1:
            return min((y1 + y2 + M), ((2 * N) + M - y1 - y2))
        if x2 == 2:
            return abs(y1 - y2)
        if x2 == 3:
            return y1 + M - y2
        if x2 == 4:
            return N + M - y1 - y2
    if x1 == 3:
        if x2 == 1:
            return y1 + y2
        if x2 == 2:
            return M - y1 + y2
        if x2 == 3:
            return abs(y1 - y2)
        if x2 == 4:
            return min((y1 + y2 + N), ((2 * M) + N - y1 - y2))
    if x1 == 4:
        if x2 == 1:
            return N + y1 - y2  
        if x2 == 2:
            return M - y2 + N - y1
        if x2 == 3:
            return min((y1 + y2 + N), ((2 * M) + N - y1 - y2))
        if x2 == 4:
            return abs(y1 - y2)

for i in range(num):
    direction, distance = map(int, input().split())
    stores.append((direction, distance))
dong_x, dong_y = map(int, input().split())
res = 0
for i in stores:
    res += check(dong_x, dong_y, i[0], i[1])
print(res)