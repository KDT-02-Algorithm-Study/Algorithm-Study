# 메모리 41536 KB, 시간 128 ms
import sys
intput = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))
h = list(map(int, input().split()))
# 자라는 길이와 나무 길이 tuple로 묶고 자라는 길이 순으로 정렬
combine = sorted((h[i], trees[i]) for i in range(n))

total = 0
for i in range(n):
    total += combine[i][0] * i + combine[i][1]
print(total)