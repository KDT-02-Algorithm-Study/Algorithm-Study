# 14889 스타트와 링크
# 37960 KB / 2832 ms

import sys
input = sys.stdin.readline

# combination
def com(start):
    if len(start) == n//2: # 종료 조건
        link = [p for p in range(n) if p not in start] # 반대쪽 팀
        a = 0
        for j in range(n):
            if j in start: # start 팀일 때
                for k in start:
                    a += g[j][k]
            else:   # link 팀일 때
                for t in link:
                    a -= g[j][t]
        result.append(abs(a))
        return
    
    index = start[-1] + 1 if start else 0
    for i in range(index, n):
        start.append(i)
        com(start)
        start.pop()

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

result = []
com([])
print(min(result)) # 최솟값 출력