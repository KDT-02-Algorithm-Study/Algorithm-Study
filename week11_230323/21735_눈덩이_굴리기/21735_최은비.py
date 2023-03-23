# 눈덩이 굴리기 https://www.acmicpc.net/problem/21735
# 31256KB / 44ms

import sys
input = sys.stdin.readline

def contest(idx, time, size):
    global ans

    # 마당 길이나 시간을 벗어나면 종료
    if idx > n-1 or time > m:
        return

    # 최대 크기를 계속해서 갱신
    ans = max(ans, size)
    
    if idx+1 < n:
        contest(idx+1, time+1, size+snow[idx+1])

    if idx+2 < n:
        contest(idx+2, time+1, size//2+snow[idx+2])



n, m = map(int, input().split())
snow = list(map(int, input().split()))
ans = 0

# 현재 눈덩이 위치, 소모 시간, 눈덩이 사이즈
# 눈덩이 시작 위치는 리스트 시작점보다 하나 작은 값이므로 -1을 입력
contest(-1, 0, 1)

print(ans)