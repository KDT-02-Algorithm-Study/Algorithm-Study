# https://www.acmicpc.net/problem/1244

import sys
input = sys.stdin.readline

n = 8
switch = [0, 0, 1, 0, 1, 0, 0, 0]
stu = 2

n = int(input())
switch = list(map(int, input().split()))
stu = int(input())

for _ in range(stu):
    students = list(map(int, input().split()))

    if students[0] == 1: # 남자
        for j in range(n):
            if (j+1) % students[1] == 0:
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1
    else: # 여자
        students[1] -= 1
        s = e = n+1
        # 좌우로 비교해주기 위해...
        # 만약 3번이면 3-1 3+1 / 3-2 3+2 이렇게 되는 거니까 뒤에 더해주고 빼는 수를 위한 for문
        for i in range(1, n//2+1):
            # 범위를 벗어나면 break
            if students[1] - i < 0 or  students[1] + i > n-1:
                break
            else:
                # 좌우가 같으면 변수를 갱신하고 다르면 그대로 break
                if switch[students[1] - i] == switch[students[1] + i]:
                    s = students[1] - i
                    e = students[1] + i
                else:
                    break
        
        # 좌우로 대칭이 있다면 s와 e는 같지 않음
        # 좌우가 대칭이라면 대칭인 구간만큼 상태를 바꾸고, 대칭이 아니라면 입력으로 들어온 스위치만 바꿈  
        if s != e:
            for i in range(s, e+1):
                if switch[i] == 1:
                    switch[i] = 0
                else:
                    switch[i] = 1
        else:
            if switch[students[1]] == 1:
                switch[students[1]] = 0
            else:
                switch[students[1]] = 1

if len(switch) > 20:
    for i in range(len(switch)):
        print(switch[i], end=" ")
        if (i+1) % 20 == 0:
            print()
else:
    print(*switch)