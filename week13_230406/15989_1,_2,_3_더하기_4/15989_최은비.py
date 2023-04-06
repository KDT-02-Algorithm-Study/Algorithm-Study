# 1, 2, 3 더하기 4 https://www.acmicpc.net/problem/15989
# 31256KB / 592ms
import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    dp = [0] * 10001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    cnt = 1
    tmp = 3

    if n > 3:
        for i in range(4, n+1):
            dp[i] = dp[i-3] + tmp

            cnt += 1

            if cnt == 3:
                cnt = 1
                tmp += 1

    print(dp[n])


'''
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4 = dp[1] + 3
dp[5] = 5 = dp[2] + 3
dp[6] = 7 = dp[3] + 4
dp[7] = 8 = dp[4] + 4
dp[8] = 10 = dp[5] + 5
dp[9] = 12 = d[6] + 5
dp[10] = 14 = dp[7] + 6
.
.
.
'''