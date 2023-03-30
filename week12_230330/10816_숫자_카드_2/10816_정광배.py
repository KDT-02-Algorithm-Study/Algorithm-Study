# 10816 숫자 카드 2
# 115664 KB / 3776 ms

# 왼쪽 끝 index
def left(lo, hi):
    if lo+1 >= hi:
        return hi
    mid = lo+hi >> 1
    if A[mid] < i:
        return left(mid, hi)
    else:
        return left(lo, mid)

# 오른쪽 끝 index
def right(lo, hi):
    if lo+1 >= hi:
        return hi
    mid = lo+hi >> 1
    if A[mid] <= i:
        return right(mid, hi)
    else:
        return right(lo, mid)

n = int(input())
A = sorted(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for i in B:
    print(right(-1, n) - left(-1, n), end=' ')