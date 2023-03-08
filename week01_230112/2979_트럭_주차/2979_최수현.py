a, b, c = map(int, input().split())
time = []
fee = 0

for i in range(3):
    x, y = map(int, input().split())
    time += list(range(x, y))

for j in range(min(time), max(time)+1):
    same_n = time.count(j)
    if same_n == 1:
        fee += a
    elif same_n == 2:
        fee += b*2
    elif same_n == 3:
        fee += c*3

print(fee)