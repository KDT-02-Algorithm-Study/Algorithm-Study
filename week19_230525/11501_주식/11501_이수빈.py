# 11501 주식
# 168032 KB / 3148ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock = stock[::-1]
    max = stock[0]
    sum = 0

    for i in range(1, N):
        if max < stock[i]:
            max = stock[i]
            continue
        sum += max - stock[i]

    print(sum)
