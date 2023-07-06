from collections import deque


# 인접행렬과 자를 와이어 인자로 전달
def bfs(arr, cut):
    check = [False] * len(arr)
    q = deque([1])
    check[1] = True
    cnt = 1
    
    while q:
        x = q.popleft()
        for connect in arr[x]:
            if connect in cut and x in cut: # 자르는 와이어인 경우 count안하고 방문처리
                check[connect] = True
            if not check[connect]:
                check[connect] = True
                q.append(connect)
                cnt += 1
    return cnt


def solution(n, wires):
    # 인접행렬 생성
    matrix = [[] for _ in range(n+1)]
    for w in wires:
        a, b = w
        matrix[a].append(b)
        matrix[b].append(a)
    
    wires.sort(key=lambda x: x[1])
    ans = 100  # 큰 수 100
    for w in wires:
        # 이어진 전력망 bfs탐색으로 count
        first = bfs(matrix, w)
        second = n - first
        ans = min(ans, abs(first-second))
    
    return ans