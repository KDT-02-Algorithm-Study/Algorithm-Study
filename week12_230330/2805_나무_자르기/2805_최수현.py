# 113752 KB, 492 ms
import sys
input = sys.stdin.readline

def cut(start, end):
    mid_h = (end + start) // 2
    mid = 0
    for tree, num in trees.items():
        if tree > mid_h:
            mid += (tree - mid_h) * num
    
    # 종료 조건
    if start > end:
        return print(mid_h)
    # 범위 좁히기
    elif mid < m:
        cut(start, mid_h-1)
    else:
        cut(mid_h+1, end)

n, m = map(int, input().split())
trees = {}
# 나무 길이와 그 개수를 딕셔너리로 저장
for h in map(int, input().split()):
    trees[h] = trees.get(h, 0) + 1

# start=0, end=가장 긴 나무
cut(0, max(trees))