# 21735 눈덩이 굴리기
# 31256KB / 40ms (# 1안으로 풀었을 경우)
# 31256KB / 52ms (# 2안으로 풀었을 경우)
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N,M = map(int,input().split())
snows = [0] + list(map(int,input().split()))

#1 
res = -1 

def dfs(idx, snow, time):
    global res
    # 제일 1순위 조건, 시간 
    if time < 0 :
        return
    # 이전것이랑 비교했을 때 제일 큰 것을 선택
    res = max(res,snow)
    if idx +1 <= N :
        dfs(idx+1,snow+snows[idx+1],time-1)
    if idx +2 <= N :
        dfs(idx+2,snow//2+snows[idx+2],time-1)

dfs(0,1,M)
print(res)

#2 
'''
def dfs(depth): 
    global res, total, snows

    # 만약 시간이 됐다면 각 경우의 수에 대한 total값을 도출
    if depth == M : 
        snow_idx,snow_val = -1,1
        for s in snow:
            if s == 0 :
                if snow_idx +1 < N : 
                    snow_idx += 1
                    snow_val += snows[snow_idx]
                else :
                    break
            elif s == 1 :
                if snow_idx +2 < N : 
                    div_snow = int(snow_val//2)
                    snow_idx += 2
                    snow_val =  div_snow + snows[snow_idx]
                    
                else :
                    break
        total.append(snow_val)
        return

    for i in range(2): # 0과 1의 경우에 수로 5번을 고를 거임 
        snow.append(i)
        dfs(depth+1) 
        snow.pop()

total,res = [],0
snow = []
dfs(0) # ,0
print(max(total)) 
'''