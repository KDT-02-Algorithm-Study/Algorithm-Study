# 1713 후보 추천하기
# 31256 KB / 48ms 
# 기본 코드

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())  # 최종 추천받을 학생의 수
mm = int(input()) # 총 투표수
vote = list(map(int,input().split())) # 투표 결과
recomm = []       # [[0,0,0] for _ in range(n)]


for v in range(mm): 
    # 0 1 2 
    min_flag = False
    for i in range(len(recomm)):
        if recomm[i][0] == vote[v]:
            recomm[i][1] += 1 
            # recomm[i][2] = v
            min_flag = True
    if min_flag == False:
        if len(recomm) <n :
            recomm.append([0,0,0])
            recomm[-1][0],recomm[-1][1],recomm[-1][2] = vote[v],recomm[-1][1]+1,v
        else :
            sorted_recomm = sorted(recomm, key = lambda x : (x[1],x[2])) 
            #print('sorted',sorted_recomm)
            selec_recomm = sorted_recomm[0] # 최소 값 구하기 
            for i in range(n):
                if recomm[i] == selec_recomm: # 최소 값 자리에 배치
                    recomm[i][0],recomm[i][1],recomm[i][2] = vote[v],1,v
    #print(recomm)
res = []
for i in recomm:
    if i[1] != 0 :
        res.append(i[0])
print(*sorted(res))

