# 2502 떡 먹는 호랑이
# 31256 KB / 200 ms

# 피보나치
def f(a, b, d):
    a = a + b
    d += 1
    # a가 K를 넘으면 False
    if a > K:
        return False
    # 날짜가 D를 넘으면 False
    if d > D:
        return False
    # 일치하면 True
    if a == K and d == D:
        return True
    
    # 재귀
    return f(b, a, d)

D, K = map(int, input().split())

# 완전 탐색
# 첫째 날(1~K) 둘째 날(1~K)
flag = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        # True면 탈출
        if f(i, j, 2):
            flag = 1
            break
    if flag:
        break
print(i, j, sep='\n')