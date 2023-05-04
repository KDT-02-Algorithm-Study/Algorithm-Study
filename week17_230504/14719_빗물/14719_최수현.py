# 31256 KB / 44 ms
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = {i: int(v) for i, v in enumerate(input().split())}
# 높은 순서로 정렬
blocks = sorted(heights.items(), key=lambda x: x[1], reverse=True)
cnt = 0

# 가장 높은 블럭부터 시작
center = left = right = blocks[0][0]

# 오른쪽의 높은 기둥 순으로 퍼져나가면서 빗물 저장
for i, v in blocks:
    if i < left:
        for j in range(i+1, left):
            cnt += v - heights[j]
        left = i
    elif i > right:
        for j in range(right+1, i):
            cnt += v - heights[j]
        right = i

print(cnt)