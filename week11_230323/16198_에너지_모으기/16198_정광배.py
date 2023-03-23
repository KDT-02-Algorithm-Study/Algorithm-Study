# 16198 에너지 모으기
# 32620 KB / 128 ms

def per(c, used, energy):
    if len(c) == n-2: # 양쪽 끝은 고르지 않으므로 n-2까지만
        result.append(energy)
        return
    
    for i in range(1, n-1):
        if not used[i]:
            
            # 사용안한 구슬을 찾을 때까지 탐색
            right = 1
            while used[i+right]:
                right+=1
            left = 1
            while used[i-left]:
                left += 1
            
            # 양쪽 계산
            energy += w[i+right]*w[i-left]

            used[i] = True
            c.append(i)
            per(c, used, energy) # 재귀
            #백트래킹
            used[i] = False
            c.pop()
            energy -= w[i+right]*w[i-left]

n = int(input())
w = list(map(int, input().split()))
used = [False]*n
result = []
per([], used, 0)
print(max(result)) # 최댓값 출력