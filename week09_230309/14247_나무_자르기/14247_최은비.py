# 14247 나무 자르기 https://www.acmicpc.net/problem/14247
# 43904KB / 152ms

import sys
input = sys.stdin.readline

n = int(input())
t_len = list(map(int, input().split())) # 첫날 나무의 높이
grow = list(map(int, input().split())) # 나무가 하루에 자라는 높이
tree = [[0, 0] for _ in range(n)] # 한 쌍으로 만들어서 하나의 리스트에 삽입
ans = 0

for i in range(n):
    tree[i] = [t_len[i], grow[i]]

# 하루에 자라는 높이가 높을 수록 나중에 자르는 게 이득
tree = sorted(tree, key=lambda x: x[1])

for i in range(n):
    # 처음 높이에 자란 높이를 더하기
    # 여기서 인덱스는 날짜에 해당하므로 곱해주기
    ans += tree[i][0] + i * tree[i][1]

print(ans)