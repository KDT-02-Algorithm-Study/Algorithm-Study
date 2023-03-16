# 1421 나무꾼 이다솜
# 31256 KB / 68 ms

import sys
input = sys.stdin.readline

# 나무 개수, 자르는 비용, 단위 가격
n, c, w = map(int, input().split())

trees = {} # 나무들을 저장할 dict
for _ in range(n):
    a = int(input())
    trees[a] = trees.get(a, 0) + 1
max_ = max(trees.keys())

# 1부터 max_까지 하나씩 확인
result = 0
for i in range(1, max_+1):
    total = 0
    for tree in trees:
        # 나무 마다 자르는 비용
        if tree%i == 0: # 나누어 떨어질 때
            cost = (tree//i-1)*c # 자른 횟수 * c
        else:           # 남을 때
            cost = (tree//i)*c # 자른 횟수 * c

        # 판매 수익보다 자르는 비용이 크면 해당 나무는 안 팔고 continue
        if (tree//i)*i*w < cost: 
            continue
        total += ((tree//i)*i*w-cost)*trees[tree]
    
    # 최댓값 조정
    if result <= total:
        result = total

print(result)