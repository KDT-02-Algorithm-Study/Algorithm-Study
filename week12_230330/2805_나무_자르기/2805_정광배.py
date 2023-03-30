# 2805 나무 자르기
# 150704 KB / 2056 ms

# 이분 탐색
def bs(lo, hi):
    if lo+1 >= hi:
        return lo
    mid = lo+hi >> 1
    if check(mid): # True면 lo=mid
        return bs(mid, hi)
    else:
        return bs(lo, mid)

# mid를 자를 때 나무 길이 더하기
def check(mid):
    sum_ = 0
    for i in d:
        if i > mid:
            sum_ += i-mid
    return sum_ >= m

n, m = map(int, input().split())
d = list(map(int, input().split()))

print(bs(0, max(d)))