# 테트리스 https://www.acmicpc.net/problem/3019
# 31256KB / 40ms
# 블럭이 바닥에 닿았을 때, 빈 칸이 없는 경우에만 cnt += 1

import sys
input = sys.stdin.readline

c, p = map(int, input().split())
field = list(map(int, input().split())) + [0] * 4
cnt = 0

for i in range(c):
    if p == 1:
        # 0도: 어디에 들어가도 빈칸이 생기지 않음
        # 무조건 cnt += 1
        cnt += 1
        # 90도: 4칸의 높이가 같아야 빈칸이 생기지 않음
        if i+3 < c and field[i] == field[i+1] == field[i+2] == field[i+3]:
            cnt +=1
    
    elif p == 2:
        # 회전해도 항상 같은 모양이므로 if로 나눠줄 필요 X
        # 두칸의 높이가 같아야 빈칸이 생기지 않음
        if i+1 < c and field[i] == field[i+1]:
            cnt += 1

    elif p == 3:
        # 0도
        if i+2 < c and field[i] == field[i+1] == field[i+2] - 1:
            cnt += 1
        # 90도
        if i+1 < c and field[i] - 1 == field[i+1]:
            cnt += 1

    elif p == 4:
        # 0도
        if i+2 < c and field[i] - 1 == field[i+1] == field[i+2]:
            cnt += 1
        # 90도
        if i+1 < c and field[i] == field[i+1] - 1:
            cnt += 1

    elif p == 5:
        # 0도
        if i+2 < c and field[i] == field[i+1] == field[i+2]:
            cnt += 1
        # 90도
        if i+1 < c and field[i] == field[i+1] - 1:
            cnt += 1
        # 180도
        if i+2 < c and field[i] - 1 == field[i+1] == field[i+2] - 1:
            cnt += 1
        # 270도
        if i+1 < c and field[i] - 1 == field[i+1]:
            cnt += 1

    elif p == 6:
        # 0도
        if i+2 < c and field[i] == field[i+1] == field[i+2]:
            cnt += 1
        # 90도
        if i+1 < c and field[i] == field[i+1]:
            cnt += 1
        # 180도
        if i+2 < c and field[i] == field[i+1] - 1 == field[i+2] - 1:
            cnt += 1
        # 270도
        if i+1 < c and field[i] - 2 == field[i+1]:
            cnt += 1

    else:
        # 0도
        if i+2 < c and field[i] == field[i+1] == field[i+2]:
            cnt += 1
        # 90도
        if i+1 < c and field[i] == field[i+1] - 2:
            cnt += 1
        # 180도
        if i+2 < c and field[i] - 1 == field[i+1] - 1 == field[i+2]:
            cnt += 1
        # 270도
        if i+1 < c and field[i] == field[i+1]:
            cnt += 1

print(cnt)