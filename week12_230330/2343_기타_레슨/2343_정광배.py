# 2343 기타 레슨
# 42340 KB / 256 ms

# 이분 탐색
def bs(lo, hi):
    if lo+1 >= hi:
        return hi
    mid = lo+hi >> 1
    if check(mid):  # True면 hi = mid
        return bs(lo, mid)
    else:
        return bs(mid, hi)

# 순서대로 탐색하면서 블루레이 개수 count
def check(mid):
    cnt = 1
    now = 0
    for i in c:
        if now + i > mid: # 초과하면 cnt+=1
            cnt += 1
            now = 0
        if i > mid: # i가 mid보다 크면 mid값 조절을 위해 False반환
            return False
        now += i
    return cnt <= m

n, m = map(int, input().split())
c = list(map(int, input().split()))

print(bs(0, max(c)*n))