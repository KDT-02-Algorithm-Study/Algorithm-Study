# 2502 떡 먹는 호랑이 https://www.acmicpc.net/problem/2502
# 시간초과.........................
# day1: A개
# day2: B개
# day3: A+B
# day4: A+2B
# day5: 2A+3B
# day6: 3A+5B
# A: 셋째날부터 피보나치수열, B: 둘째날부터 피보나치수열

import sys
input = sys.stdin.readline

def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

day, tteok = map(int, input().split())
a = fibo(day-3)
b = fibo(day-2)
breaker = False

for i in range(1, tteok+1):
    for j in range(1, i+1):
        if (a*j + b*i) == tteok:
            print(j, i, sep="\n")
            breaker = True
            break

    if breaker:
        break