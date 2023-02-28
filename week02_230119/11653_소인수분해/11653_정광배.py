# 11653 소인수분해
N = int(input())

graph = [0] * (N+1) # 저장할 테이블
for i in range(2, N+1):
    if graph[i] == 0: # 아직 체크한 값이 아니면
        while True:
            if N % i == 0: # 나눠지면
                print(i)   # 출력
                for j in range(i, N+1, i): # i의 배수를
                    graph[j] = 1        # 테이블에 체크하기
                N //= i
            else:
                break