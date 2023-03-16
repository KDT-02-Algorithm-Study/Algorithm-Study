# 틀렸는데 사실 문제가 이해가 잘 안됩니다..😭

N, C, W = map(int, input().split())
total = 0

for _ in range(N):
    wood = int(input())
    revenue = wood * W - C
    if revenue > 0:
        total += revenue

print(total)