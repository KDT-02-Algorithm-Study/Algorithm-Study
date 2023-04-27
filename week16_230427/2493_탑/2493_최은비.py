# 탑 https://www.acmicpc.net/problem/2493
# 104620KB / 732ms
import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
# 수신 가능성이 있는 탑들의 인덱스와 높이를 튜플로 저장
height = []

for i in range(n):
    if height:
        while height:
            # 현재 탑보다 높은 탑이 나올 때까지 pop
            if tower[i] < height[-1][1]:
                print(height[-1][0]+1, end=" ")
                break

            height.pop()

    # 현재 탑보다 높은 탑이 없으면 0 출력
    if not height:
        print(0, end=" ")

    # 현재 탑도 다음 탑이 보낸 신호를 수신할 가능성이 있으니까 append
    height.append((i, tower[i]))
