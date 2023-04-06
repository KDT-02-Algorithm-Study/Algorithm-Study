# 회전 초밥 https://www.acmicpc.net/problem/2531
# 34160KB / 3436ms
import sys
from collections import deque
input = sys.stdin.readline

# 벨트에 놓인 초밥 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
n, d, k, c = map(int, input().split())
# 벨트에 놓인 초밥 입력
sushi = deque([int(input()) for _ in range(n)])
# 내가 먹은 초밥을 입력할 deque
dish = deque()
s = 0
e = 0
ans = 0

# s가 초밥 리스트를 다 돌 때까지 반복
while s < n:
    # 원형 벨트니까 sushi[0]과 sushi[-1]이 한 리스트에 담길 수 있게 나머지를 인덱스로 넣어줌
    dish.append(sushi[e%n])

    # 내가 먹은 초밥 수가 k개고
    if e - s == k-1:
        # 그 초밥 중에 쿠폰이 없으면 종류에 +1
        if c not in dish:
            ans = max(ans, len(set(dish))+1)
        # 이미 동일한 초밥을 먹었으면 내가 먹은 초밥 종류만
        else:
            ans = max(ans, len(set(dish)))

    # 내가 먹은 초밥 수가 k개보다 작으면 더 먹어야 함
    if e == s or e - s < k:
        e += 1
    # k개보다 많으면 하나를 버려야 함
    else:
        s += 1
        dish.popleft()

print(ans)