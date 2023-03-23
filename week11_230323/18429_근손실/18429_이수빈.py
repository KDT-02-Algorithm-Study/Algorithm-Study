# 18429 근손실
# 31256 KB / 84ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n,k = map(int,input().split())
weights = list(map(int,input().split()))

def dfs(base):
    global cnt, weights

    # n개 이상 & 조건에 만족하기 때문에 cnt += 1
    if len(track) == n :
        # print(track)
        cnt += 1    
        return

    # 중복이 안되는 순서를 생성 
    for i in range(n):
        # True인 경우에는 실행 안 함 
        if visited[i] :
            continue
        
        # False인 경우 + 중량 합이 500인 경우에만 계산
        next_base = base + weights[i] -k
        if next_base >= 500 : 
            visited[i] = True
            track.append(next_base)
            dfs(next_base)
            track.pop()
            visited[i] = False

visited = [False]*n
track,cnt = [],0
dfs(500)
print(cnt)

# 백준 1등 코드 
# 31256KB / 52ms
# append / pop을 안씀
'''
def dfs(cnt, total):
    global res
    # 최상위 조건을 500으로 둠 
    if total < 500:
        return
    # 500이 넘으면, 조건을 넣어줌.. 무슨 의미인지 잘 모르겠음 
    # 아무튼 pop append 말고 다른 for로 넣으면 시간을 더 줄일 수 있음
    if total-(N-cnt)*K >= 500:
        temp = 1
        for i in range(1, N-cnt+1):
            temp *= i
        res += temp
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(cnt+1, total+A[i]-K) # depth가 1이고, 현재 중량이 다음과 같음 
            visited[i] = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [0]*N
res = 0
dfs(0, 500)
print(res)

'''

# 백준 2등 코드 
# 30616KB / 60ms
# append / pop 안 써도 되나봄.. 
'''
N,K=map(int,input().split())
L=list(map(int,input().split()))

visit=[False]*(N)
Answer=0
def BackTracking(deep , total):
    global Answer
    if total<300: # 안넘으면 고려 안 하고 
        return

    if deep==N: # depth가 3이면 
        Answer+=1
        return

    for i in range(N):
        if not visit[i]:
            visit[i]=True
            BackTracking(deep+1 , total+L[i]-K) # depth와 total에 대해 바로 dfs로 넣기
            visit[i]=False
BackTracking(1,300) # 500인데..? 뭐지 

print(Answer)

'''