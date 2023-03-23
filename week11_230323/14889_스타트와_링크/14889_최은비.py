# 스타트와 링크 https://www.acmicpc.net/problem/14889
# 시간초과를 해결하지 못했습니다..............
import sys
input = sys.stdin.readline

def team(cnt, start):
    global res

    if cnt == n//2:
        start = 0
        link = 0

        for i in range(n):
            for j in range(i+1, n):
                if check[i] and check[j]:
                    start += graph[i][j]
                    start += graph[j][i]
                elif not check[i] and not check[j]:
                    link += graph[i][j]
                    link += graph[j][i]

        res = min(res, abs(start - link))
        return

    for i in range(start, n):
        if check[i]:
            continue

        check[i] = True
        team(cnt+1, start+1)
        check[i] = False


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
check = [False] * n
res = int(1e9) 

team(0, 0)

print(res)