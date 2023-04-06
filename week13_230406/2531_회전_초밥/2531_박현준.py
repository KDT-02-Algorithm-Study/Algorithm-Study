# 시간초과

N, d, k, c = map(int, input().split())

lst = [int(input()) for _ in range(N)]
res = 0

for i in range(N):
    # 서비스 맛있다
    cnt = 1
    visited = [False] * (d+1)
    visited[c] = True
    for j in range(i, i+k):
        sushi = lst[j % N]
        if not visited[sushi]:
            cnt += 1
        visited[sushi] = True
    if res < cnt:
        res = cnt
print(res)