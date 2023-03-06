# https://www.acmicpc.net/problem/1193
# line이 짝수면 1/n ~ n/1 순서로, 홀수면 n/1 ~ 1/n 순서로 진행되기 때문에 
# gap으로 line의 몇 번째 분수인지를 찾는 것

import sys
input = sys.stdin.readline

num = int(input())
line = 0
cnt = 0

if num == 1:
    print(1, "/", 1, sep="")
else:
    while num > cnt:
        line += 1
        cnt += line

    gap =  line - (cnt - num)

    if line % 2 == 0:
        top = gap
        bottom = line - gap + 1
    else:
        top = line - gap + 1
        bottom = gap

    print(top, "/", bottom, sep="")