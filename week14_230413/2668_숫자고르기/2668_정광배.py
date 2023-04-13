# 2668 숫자고르기
# 31256 KB / 40 ms

import sys
input = sys.stdin.readline

def dfs(x,now):
    stack = [(x,now)]
    v[x] = True
    while stack:
        x, now = stack.pop()
        now.append(x)
        for j in g[x]:
            # 현재 탐색에 없는 경우
            if j not in now:
                v[j] = True
                stack.append((j, now.copy()))
            else: # 현재 탐색에 있는 경우(cycle 발생)
                result.append(now)
                return

n = int(input())
g = [[] for _ in range(n+1)]
v = [False]*(n+1)
for i in range(1, n+1):
    a = int(input())
    g[a].append(i)

# 탐색하면서 cycle일 경우 result에 저장
result = []
for i in range(1, n+1):
    if not v[i]:
        dfs(i,[])

# 합하고 정렬후 len과 요소 출력
result = sum(result,[])
result.sort()
print(len(result))
print('\n'.join(map(str,result)))