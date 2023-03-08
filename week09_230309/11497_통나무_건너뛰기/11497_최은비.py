# 11497 통나무 건너뛰기 https://www.acmicpc.net/problem/11497
# 32276KB / 292ms
# 통나무 길이를 오름차순으로 정렬 후 새로운 리스트에 삽입
# 삽입 순서는 (인덱스 기준) 0, n-1, 1, n-2, 2, n-3, ...

import sys
input = sys.stdin.readline

test = int(input())

for t in range(test):
    n = int(input()) # 통나무 개수
    tree = sorted(list(map(int, input().split()))) # 통나무 높이를 입력 받고 오름차순으로 정렬
    sorted_tree = [0] * n
    left = 0
    right = n-1
    ans = 0

    for i in range(n):
        if i % 2 == 0:
            sorted_tree[left] = tree[i]
            left += 1
        else:
            sorted_tree[right] = tree[i]
            right -= 1

    # 정렬된 리스트를 순회하면서 최대 차이 구하기
    for i in range(n-1):
        ans = max(ans, abs(sorted_tree[i]-sorted_tree[i+1]))

    print(ans)