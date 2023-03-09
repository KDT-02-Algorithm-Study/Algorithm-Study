# 메모리 32276 KB, 시간 192? 180? ms
import sys
intput = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    trees = sorted(list(map(int, input().split())))
    
    # 작은 통나무 두개와 가장 큰 통나무 두개의 길이차이 중 큰것
    level = max(trees[1]-trees[0], trees[-1]-trees[-2])

    # 양쪽 번갈아가며 배치(인덱스 2씩 차이남)
    for i in range(2, n):
        if trees[i] - trees[i-2] > level:
            level = trees[i] - trees[i-2]
    
    print(level)