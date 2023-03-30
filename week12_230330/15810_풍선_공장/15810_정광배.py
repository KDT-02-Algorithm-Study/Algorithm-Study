# 15810 풍선 공장
# 150704 KB / 1656 ms

# 이분 탐색
def bs(lo, hi):
    if lo + 1 >= hi: # 탈출 조건
        return hi

    mid = lo + hi >> 1
    
    if check(mid): # True면 hi = mid
        return bs(lo, mid)
    else:
        return bs(mid, hi)

# 
def check(mid):
    sum_ = 0
    for i in a:
        sum_ += mid//i # (시간 // 한 사람 처리시간) = 한 사람이 시간안에 처리한 양
    return sum_ >= m

n, m = map(int, input().split())
a = list(map(int, input().split()))

print(bs(0, max(a)*m))