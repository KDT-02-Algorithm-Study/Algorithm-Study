# 2846 오르막길

N = int(input())
p = list(map(int, input().split()))
step = 0 # 높이 차이
result = 0 # 높이 중에 큰 값
for data in range(N-1):
    # 오르막이면
    if p[data+1] > p[data]:
        step += p[data+1] - p[data] # 높이 차이 저장
    else: # 내리막이거나 같은 높이라면 step 초기화
        step = 0
    result = max(result, step) # 기존 높이와 현재 높이 중 큰 값
print(result)