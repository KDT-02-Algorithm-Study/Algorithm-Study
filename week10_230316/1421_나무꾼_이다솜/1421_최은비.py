# 1421 나무꾼 이다솜 https://www.acmicpc.net/problem/1421
# 틀렸습니다......

import sys
input = sys.stdin.readline

n, cut_cost, sell_cost = map(int, input().split())
tree = [int(input()) for _ in range(n)]
res = 0

for i in range(1, 1001):
    tmp_sum = 0
    for j in range(n):
        cnt = tree[j] // i # 자르고 난 나무 개수
        rest = tree[j] % i # 버려지는 길이

        if rest:
            cut = cnt * cut_cost
        else:
            cut = (cnt-1) * cut_cost

        tmp = i * cnt * sell_cost - cut

        if tmp > 0:
            tmp_sum += tmp

    if tmp_sum > res:
        res = tmp_sum

print(res)