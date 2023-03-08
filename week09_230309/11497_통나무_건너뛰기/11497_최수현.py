# 메모리 32276 KB, 시간 192? 180? ms
import sys
intput = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    trees = sorted(list(map(int, input().split())))
    
    level = max(trees[1]-trees[0], trees[-1]-trees[-2])
    for i in range(2, n):
        if trees[i] - trees[i-2] > level:
            level = trees[i] - trees[i-2]
    
    print(level)