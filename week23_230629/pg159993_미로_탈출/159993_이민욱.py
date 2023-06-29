# 프로그래머스 159993 미로 탈출

from collections import deque
d = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x,y,n,m,g,le,end):      # bfs 최단거리 구하기
    q = deque([(x,y)])
    vi = [[0] * m for _ in range(n)]
    vi[x][y] = 1
    while q:
      x,y = q.popleft()
      for dx,dy in d:
        nx,ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] in ('S','O','L','E'):
          if not vi[nx][ny]:
            vi[nx][ny] = vi[x][y] + 1
            q.append((nx,ny))

    return vi[le[0]][le[1]], vi[end[0]][end[1]] # 레버까지 거리, 레버부터 출구까지 거리

def solution(maps):
    answer = 0
    n = len(maps)       # 행 길이
    m = len(maps[0])    # 열 길이

    for i in range(len(maps)):
      for j in range(len(maps[0])):
        if maps[i][j] == 'S':
          st = (i,j)            # 시작점 인덱스
        elif maps[i][j] == 'L':
          le = (i,j)            # 레버 인덱스
        elif maps[i][j] == 'E':
          end = (i,j)           # 출구 인덱스
    
    ans_le, ans_end = bfs(st[0],st[1],n,m,maps,le,end)      # 시작점에서 시작
    answer += ans_le - 1
    ans_le2, ans_end2 = bfs(le[0],le[1],n,m,maps,le,end)    # 레버부터 시작
    answer += ans_end2 - 1

    if ans_le and ans_end2:     # 둘 다 존재하면 탈출 완료
      return answer
    else:                       # 탈출 실패
      return -1

# 테스트 1 〉	통과 (0.11ms, 10.2MB)
# 테스트 2 〉	통과 (0.12ms, 10.2MB)
# 테스트 3 〉	통과 (0.39ms, 10.1MB)
# 테스트 4 〉	통과 (0.17ms, 10.1MB)
# 테스트 5 〉	통과 (0.17ms, 10MB)
# 테스트 6 〉	통과 (0.22ms, 10.2MB)
# 테스트 7 〉	통과 (2.07ms, 10.2MB)
# 테스트 8 〉	통과 (3.15ms, 10.2MB)
# 테스트 9 〉	통과 (0.07ms, 10.1MB)
# 테스트 10 〉	통과 (0.03ms, 10MB)
# 테스트 11 〉	통과 (1.77ms, 10.2MB)
# 테스트 12 〉	통과 (7.12ms, 10.2MB)
# 테스트 13 〉	통과 (7.36ms, 10.1MB)
# 테스트 14 〉	통과 (7.00ms, 10.1MB)
# 테스트 15 〉	통과 (0.76ms, 10MB)
# 테스트 16 〉	통과 (19.51ms, 10.2MB)
# 테스트 17 〉	통과 (23.94ms, 10.2MB)
# 테스트 18 〉	통과 (0.37ms, 10MB)
# 테스트 19 〉	통과 (0.20ms, 10.2MB)
# 테스트 20 〉	통과 (19.83ms, 10.1MB)
# 테스트 21 〉	통과 (1.89ms, 10.1MB)
# 테스트 22 〉	통과 (0.18ms, 10.1MB)
# 테스트 23 〉	통과 (0.09ms, 10.2MB)