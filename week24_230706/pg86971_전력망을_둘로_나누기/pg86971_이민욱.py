# 프로그래머스 86971 전력망을 둘로 나누기

from collections import deque

def bfs(x,g,vi):        # bfs로 연결된 송전탑 개수 구하기
    q = deque([x])
    vi[x] = 1
    cnt = 1

    while q:
        now = q.popleft()
        
        for i in g[now]:
            if not vi[i]:
                vi[i] = 1
                cnt += 1
                q.append(i)
                
    return cnt

def solution(n, wires):
    answer = n
    g = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:         # 노드 생성
        g[v1].append(v2)
        g[v2].append(v1)
            
    for a,b in wires:           # 간선 정보를 꺼내서
        vi = [0] * (n+1)        # 방문 리스트
        vi[b] = 1               # b를 방문처리해서 a-b 간선을 없앰
        cnt = bfs(a,g,vi)       # a와 연결된 송전탑 개수 구하는 bfs 실행
        answer = min(answer, abs(cnt - (n-cnt)))    # 최솟값 갱신
        
    return answer

# 테스트 1 〉	통과 (0.24ms, 10.1MB)
# 테스트 2 〉	통과 (1.20ms, 10.2MB)
# 테스트 3 〉	통과 (1.93ms, 10.2MB)
# 테스트 4 〉	통과 (3.84ms, 10.3MB)
# 테스트 5 〉	통과 (2.07ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.07ms, 9.94MB)
# 테스트 9 〉	통과 (0.05ms, 10.1MB)
# 테스트 10 〉	통과 (1.25ms, 10.2MB)
# 테스트 11 〉	통과 (1.12ms, 10.3MB)
# 테스트 12 〉	통과 (1.94ms, 10.2MB)
# 테스트 13 〉	통과 (1.93ms, 10.2MB)