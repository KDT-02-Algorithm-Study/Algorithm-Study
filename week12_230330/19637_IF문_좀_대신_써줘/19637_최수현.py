# 50264 KB, 624 ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tier = {}

# 전투력과 칭호를 딕셔너리로 저장
for _ in range(n):
    name, score = input().split()
    if int(score) not in tier:
        tier[int(score)] = name

# 전투력 정렬
level = sorted(tier.keys())
power = [int(input()) for _ in range(m)]

# 각각 캐릭터의 전투력마다 이분탐색하기
for p in power:
    start = 0
    end = len(level) - 1
    my_level = 0

    while start <= end:
        mid = (start + end) // 2

        if level[mid] >= p:
            my_level = level[mid]
            end = mid -1
        else:
            start = mid + 1
        
    print(tier[my_level])