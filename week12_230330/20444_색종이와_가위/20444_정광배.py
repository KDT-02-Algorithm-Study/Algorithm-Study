# 20444 색종이와 가위
# 31256 KB / 40 ms

# 이분 탐색
def bs(start, end):
    if start > end:
        return 'NO'
    mid = start + end >> 1
    if (mid+1)*(n-mid+1) < k:
        return bs(mid+1, end)
    elif (mid+1)*(n-mid+1) > k:
        return bs(start, mid-1)
    else:
        return 'YES'

n, k = map(int, input().split())

print(bs(0, n//2+1))