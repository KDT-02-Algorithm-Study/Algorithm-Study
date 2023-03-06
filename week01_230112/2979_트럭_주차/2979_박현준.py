A, B, C = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(3)]
Max = max(time[0][1], time[1][1], time[2][1])
parking = [0] * (Max-1)
sum = 0

for i in range(3):
    for j in range(time[i][0]-1, time[i][1]-1):
        parking[j] += 1

for i in parking:
    if i == 1:
        sum += i*A
    if i == 2:
        sum += i*B
    if i == 3:
        sum += i*C
print(sum)