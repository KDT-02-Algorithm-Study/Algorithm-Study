import sys

def pooling(matrix, l):
    if l == 1:
        print(matrix[0][0])
        return
    
    small_m = [[] for _ in range(l//2)]
    for y in range(0, l, 2):
        for x in range(0, l, 2):
            twotwo = [matrix[y+dy][x+dx] for dy, dx in delta]
            twotwo.sort(reverse=True)
            small_m[y//2].append(twotwo[1])
    
    pooling(small_m, l//2)

n = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
delta = [(0, 0), (0, 1), (1, 0), (1, 1)]
pooling(matrix, n)