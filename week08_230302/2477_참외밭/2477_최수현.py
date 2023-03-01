# 메모리 31256 KB, 시간 44 ms
import sys
intput = sys.stdin.readline

n = int(input())
# 튜플로 저장
farm = [tuple(map(int, input().split())) for _ in range(6)]

for i in reversed(range(6)):
    # i, i-1의 방향이 i-2, i-3의 방향과 같다면 큰 직사각형에서 i-1, i-2의 땅크기 빼기
    if farm[i][0] == farm[i-2][0] and farm[i-1][0] == farm[i-3][0]:
        print(n * (farm[i-4][1] * farm[i-5][1] - (farm[i-1][1] * farm[i-2][1])))