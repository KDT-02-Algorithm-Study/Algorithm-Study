# 1459 걷기 https://www.acmicpc.net/problem/1459
# 31256KB / 40ms

import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())
ans = 0

# 직선으로 두번 이동한 시간보다 대각선으로 이동한 시간이 적은 경우
# 최소 시간이 되기 위해서는 대각선으로 최대한 많이 이동해야 함
if x != 0 and y != 0:
    if w * 2 > s:
        if x > y:
            ans += s * y
            x -= y
            y = 0
            
        else:
            ans += s * x
            tmp = y-x
            y -= x
            x = 0
            
# 이제 직선으로만 이동해야 하는데, 직선으로 두칸을 이동하거나 대각선으로 두칸을 이동할 수 있음
# 직선으로 두번 이동했을 때보다 대각선으로 두번 이동했을 때가 적은 시간이 걸리는 경우
if w > s:
    tmp = x // 2
    ans += s * tmp * 2
    x -= tmp * 2
    tmp = y // 2
    ans += s * tmp * 2
    y -= tmp * 2

# 이제 더이상 대각선으로 이동할 수 없음
ans += w * (x + y)

print(ans)