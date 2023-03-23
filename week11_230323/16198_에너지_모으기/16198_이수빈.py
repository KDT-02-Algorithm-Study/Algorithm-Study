# 16198 에너지 모으기
# readline 안 쓰고 있음.. 회사에 따라서 sys 못 쓰는 곳도 있다고 하길래! 
# 	32620 KB / 92ms (구한 값들을 모두 append 해서 print부분에 max)
# 	31256 KB / 92ms (실시간으로 max_ball 구하기 / 메모리에서 유리)
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# visited가 꼭 필요한 것은 아님 
# 풀면서 자연스럽게 중복을 허용하지 않는다면 없어도 상관 없을 듯 

N = int(input())
balls_raw = list(map(int,input().split()))
balls = balls_raw

def dfs(depth,ball):
    global balls, max_ball
    
    # 조건식을 달아줘야하고..
    if depth == N-2 : 
        if ball >= max_ball :
            max_ball = ball 
        # balls = balls_raw 
        # 원래는 복구를 여기서 해줬는데.. 이건 의미가 없는 듯
        # 복구는 dfs 식 끝난 후에 해주기 
        # visited할 때도 dfs 전 후로 append pop 해주는 것처럼 
        return
    
    # 기본 재귀식을 달아줘야하고.. 
    for i in range(1,len(balls)-1):
        next_ball = ball + (balls[i-1]*balls[i+1])
        b = balls.pop(i)
        dfs(depth+1,next_ball)
        # 복구해주는 작업이 꼭 필요함 
        balls.insert(i,b)

max_ball = 0 
dfs(0,0)
print(max_ball)    


# 백준 상위 랭커 코드 
'''
"""
3. 분할-정복 기법으로 풀기
5
100 2 1 3 100
"""

n = int(input())
bids = list(map(int, input().split()))

def divide_conquer(arr):
    if len(arr) == 3:
        return arr[0]*arr[2]

    ret = 0 # 최댓값 0부터 시작함
    for i in range(1, len(arr) - 1):
        # 현재 i번째 구슬을 선택하고 에너지를 계산한 뒤 나머지 구슬들을 대상으로 다시 탐색들어감
        ret = max(ret,arr[i-1]*arr[i+1] + divide_conquer(arr[:i]+arr[i+1:]))
    return ret

ans = divide_conquer(bids)
print(ans)

'''