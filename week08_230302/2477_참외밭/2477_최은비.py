# 참외밭 https://www.acmicpc.net/problem/2477
# 31256KB, 40ms

import sys
input = sys.stdin.readline

n = int(input())
field = [(0, 0)] * 6 # 밭 둘레의 방향과 길이를 튜플로 저장할 리스트
cnt = [0] * 5 # 방향 등장 횟수를 저정할 리스트
total = 1 # 전체 넓이
sub = 1 # 작은 사각형 넓이

for i in range(6):
    direction, length = map(int, input().split())
    field[i] = (direction, length)
    cnt[direction] += 1

for i in range(6):
    # 한 번씩 등장한 방향이면 전체 넓이에 해당하는 사각형 둘레이므로 total에 곱해주기
    if cnt[field[i][0]] == 1:
        total *= field[i][1]
    
    else:
        # 아니라면 하나 건너서 일치하는지 확인하고
        # 일치한다면 그 사이에 있는 값이 작은 사각형 둘레이므로 sub에 곱해주기
        if field[i][0] == field[(i+2)%6][0]:
            sub *= field[(i+1)%6][1]

print((total - sub) * n)