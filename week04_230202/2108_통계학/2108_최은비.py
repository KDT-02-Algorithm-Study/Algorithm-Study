# https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers = sorted(numbers)
num_dict = {}

for num in numbers:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)

mode = num_dict[0][0]

if len(num_dict) > 1:
    if num_dict[0][1] == num_dict[1][1]:
        mode = num_dict[1][0]


avg = round(sum(numbers) / n)
mid = numbers[n//2]
range_ = numbers[-1] - numbers[0]

print(avg, mid, mode, range_, sep="\n")