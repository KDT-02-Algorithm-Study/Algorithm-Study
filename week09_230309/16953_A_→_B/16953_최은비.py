# 16953 A → B  https://www.acmicpc.net/problem/16953
# 31256KB / 40ms

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1 # 연산 횟수를 저장할 변수

# b를 a로 만들 수 있는지를 판단
while True:
    # 반복문 탈출 조건
    if a >= b:
        break

    # b의 마지막 수가 1이면 1을 떼고 연산 횟수 +1
    if b % 10 == 1:
        b //= 10
        cnt += 1

    # b가 2로 나누어지면 2로 나누고 연산 횟수 +1
    elif b % 2 == 0:
        b //= 2
        cnt += 1

    # 위에 두 조건을 만족하지 못하면 반복문 종료
    else:
        break

# 반복문을 나왔을 때 a와 b가 다르면 만들 수 없는 수이므로 -1 
if a != b:
    cnt = -1

print(cnt)