# 숫자고르기 https://www.acmicpc.net/problem/2668
# 31256KB / 40ms
import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    idx.add(x)
    val.add(num[x])
    
    if not visited[num[x]]:
        dfs(num[x])
    else:
        return


n = int(input())
num = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n+1)
idx = set([]) # 첫째줄
val = set([]) # 둘째줄
res = [] # 결과

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        # 첫째줄과 둘째줄 원소가 같으면
        if idx == val:
            for j in idx:
                if j not in res:
                    res.append(j)

        else:
            for j in idx:
                visited[j] = False
    
    idx.clear()
    val.clear()

print(len(res))
print(*res, sep='\n')