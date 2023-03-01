# 2979

import sys

price1, price2, price3 = map(int, sys.stdin.readline().split())
truck = [0] * 100
total = 0

for i in range(3):
    in_hour, out_hour = map(int, sys.stdin.readline().split())
    for j in range(in_hour, out_hour):
        truck[j] += 1

for i in range(len(truck)):
    if truck[i] == 1:
        total += truck[i] * price1
    elif truck[i] == 2:
        total += truck[i] * price2
    elif truck[i] == 3:
        total += truck[i] * price3

print(total)