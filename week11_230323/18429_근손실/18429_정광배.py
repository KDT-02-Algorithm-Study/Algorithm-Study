# 18429 근손실
# 31256 KB / 80 ms

def per(used, day, weight):
    global r
    if day == n: # 마지막 날 일때
        r += 1
        return
    
    weight -= k # 중량 감소
    for i in range(n):
        if not used[i]: # 사용하지 않은 수일 때
            if weight+a[i] >= 0: # 운동 후 음수가 아닐 때만
                used[i] = True
                per(used, day+1, weight+a[i])
                used[i] = False # 백트래킹

n, k = map(int, input().split())
a = list(map(int, input().split()))
used = [False] * n # visited
r = 0 # 경우의 수 count
per(used,0,0)
print(r)