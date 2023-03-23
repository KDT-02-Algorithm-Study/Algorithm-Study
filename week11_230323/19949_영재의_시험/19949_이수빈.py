# 19949 영재의 시험
# 122456 KB / 1384 ms (pypy3로 제출..)
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

answer = list(map(int,input().split()))

# 영재 답안 생성기
def dfs() :
    global score, yj_q

    # 만약 갯수가 10개가 모이면 
    if len(yj_q) == 10 : 
        cnt = 0 # 얘는 답안마다 새로운 애니까 초기화 
        for k in range(10):
            if yj_q[k] == answer[k] : # 같으면 cnt += 1
                cnt += 1 
            if cnt >= 5 : # 5점 이상이면 그냥 scroe +=1하고 끝
                score +=1
                break
        return 

    # 영재 답안 만들기  
    for j in range(1,6):
        if len(yj_q) > 1 and yj_q[-1] == yj_q[-2] == j : # 만약 연속이 된다면 
            continue
        yj_q.append(j)
        dfs()
        yj_q.pop()

yj_q,score = [],0
dfs()
print(score)