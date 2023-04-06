# 31256 KB / 68 ms
import sys
input = sys.stdin.readline

n = int(input())
pillar = [tuple(map(int, input().split())) for _ in range(n)]
# 기둥이 큰 순서대로 정렬
pillar.sort(key=lambda x: x[1], reverse=True)

# 가장 큰 기둥의 길이만큼 total에 더해주고 시작
total = pillar[0][1]
# 왼쪽, 오른쪽으로 움직일 flag를 가장 큰 기둥의 좌표에서 시작
flag = left_f = right_f = pillar[0][0]

for i in range(1, n):
    x, y = pillar[i]
    # 좌표가 가장 큰 기둥의 왼쪽에 있으면서 left flag 좌표보다 작은 경우
    if x < flag and x < left_f:
        total += (left_f - x) * y
        left_f = x
    # 좌표가 가장 큰 기둥의 오른쪽에 있으면서 right flag 좌표보다 큰 경우
    elif x > flag and x > right_f:
        total += (x - right_f) * y
        right_f = x

print(total)