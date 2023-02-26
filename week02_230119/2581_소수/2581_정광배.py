#2581 소수

M = int(input())
N = int(input())

graph = [0] * (N+1) # 저장할 테이블
graph[1] = 1 # 1은 소수가 아님
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if j == i:  # 소수는 그냥 넘김
            continue
        else:           # 소수의 배수는
            graph[j] = 1 # 테이블에 체크

# M ~ M의 테이블에서 체크 안된 것 추출
result = []
for x in range(N-M+1):
    if graph[x+M] == 0:
        result.append(x+M)
### List Comprehension ###
# result = [x for x in range(M, N+1) if graph[x] == 0]

if result:
    print(sum(result), min(result), sep='\n')
else:
    print(-1)