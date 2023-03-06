# https://www.acmicpc.net/problem/1436
# 666부터 1씩 더해가면서 '666'이 들어있는지 판별
# 만약 들어있으면 cnt에 1을 더하고 그 cnt가 입력된 num과 같으면 while문 종료

import sys
input = sys.stdin.readline

num = int(input().strip())
cnt = 0
movie = 666

while True:
    if str(movie).count("666") >= 1:
        cnt += 1

        if cnt == num:
            break

    movie += 1

print(movie)
