# 11497 통나무 건너뛰기
# 32276 KB / 276 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(T):
    log = int(input())
    log_nums = list(map(int,input().split()))
    sort_log_nums = sorted(log_nums,reverse=True)

    new_logs = [0]*log
    # 홀수일 때
    if log % 2 != 0 :
        idx = 0 
        for i in range(log):
            llog = sort_log_nums[i] # 9 7 5
            if i % 2 != 0 :
                idx += 1 # 1 
                idx = idx*(-1)
            elif i > 0 and i % 2 == 0 :
                idx = idx*(-1)
            new_logs[(log//2) - idx] = llog    
    # 짝수일 때    
    else : 
        for j in range(log//2):
            # 0 1 2 3
            new_logs[(log//2) + j] = sort_log_nums[(j*2)+1]
        for jj in range(log//2):
            # 0 1 2 3
            new_logs[((log//2)-1) - jj] = sort_log_nums[jj*2]

    diff_log = []
    # 최대 차이 구하기
    for p in range(1,log):
        diff_log.append(abs(new_logs[p-1]-new_logs[p]))

    print(max(diff_log))