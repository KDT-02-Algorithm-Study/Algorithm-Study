# 14889 스타트와 링크
# 31256 KB / 7672 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 해당 문제의 key point 
# 시간 복잡도 해결 방안 능력 
# for문에 대한 조건 탐색 




N = int(input())
effort = [list(map(int,input().split()))for _ in range(N)]
min_diff = 1e9
s,l = [],[]

def dfs(depth, idx): 
    global min_diff
    # depth 기준 기반 팀 나누기   
    if depth == N//2:
        # print(visited)
        s_effort,l_effort = 0,0

        # 능력치 구하기
        # 오름차순으로 for문을 구현해서 반복문의 조건을 좁히기 
        for i in range(N-1):
            for j in range(i+1,N):
                if visited[i] == True and visited[j] == True:
                    s_effort += effort[i][j] # 그 대신 뒤집어서도 더해주기 
                    s_effort += effort[j][i]
                elif visited[i] == False and visited[j] == False:
                    l_effort += effort[i][j]
                    l_effort += effort[j][i]
        # 최소치 구하기 
        min_diff = min(min_diff,abs(s_effort-l_effort))

    # 중복 없는 수열을 구하기 위함  
    for i in range(idx, N): # 그냥 1~N까지 돌면, 중복 고려 안하고, 모든 i를 출력 
        if visited[i]: # idx부터 돌면, 이미 사용했었던 i는 활용 안해도 됨 
            continue
        visited[i] = True
        dfs(depth+1, i+1)
        visited[i] = False
        
visited = [False]*(N)
dfs(0,0)
print(min_diff)


# 시간 초과 1
# append로 인해 나는 것인지 하여 2안으로 진행
'''
N = int(input())
effort = [list(map(int,input().split()))for _ in range(N)]
min_diff = 1e9

def dfs(depth):
    global min_diff
    # depth 기준 기반 팀 나누기   
    if depth == N:
        # 팀 나누기 
        s,l = stack[:N//2],stack[N//2:]
        s_effort,l_effort = 0,0
        
        # 능력치 구하기
        for j in range(N//2):
            for k in range(N//2):
                
                s_effort += effort[s[j]][s[k]]
                l_effort += effort[l[j]][l[k]]
        
        # 최소치 구하기 
        min_diff = min(min_diff,abs(s_effort-l_effort))
        return

    # 중복 없는 수열을 구하기 위함  
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(i)
        dfs(depth+1)
        stack.pop()
        visited[i] = False
        
visited = [False]*(N)
stack=[]
dfs(0)
print(min_diff)

'''

# 시간 초과 2
# append를 지우고 통합했는데도 불구하고 시간초과.. 
# 구글링을 해본 결과 시간 효율이 중요해서 for문에 대한 조건을 줄여줘야한다고 함 
'''
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
effort = [list(map(int,input().split()))for _ in range(N)]
min_diff = 1e9
s,l = [],[]

def dfs(depth):
    global min_diff
    # depth 기준 기반 팀 나누기   
    if depth == N//2:
        # 팀 나누기 
        s_effort,l_effort = 0,0
        #print(visited)
        
        # 능력치 구하기
        for j in range(N):
            for k in range(N):
                if visited[j] == True and visited[k] == True:
                    #print('stark',j,k)
                    s_effort += effort[j][k]
                elif visited[j] == False and visited[k] == False:
                    #print('link',j,k)
                    l_effort += effort[j][k]
        #print(s_effort,l_effort,min_diff)
        # 최소치 구하기 
        min_diff = min(min_diff,abs(s_effort-l_effort))

    # 중복 없는 수열을 구하기 위함  
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        dfs(depth+1)
        visited[i] = False
        
visited = [False]*(N)
dfs(0)
print(min_diff)

'''