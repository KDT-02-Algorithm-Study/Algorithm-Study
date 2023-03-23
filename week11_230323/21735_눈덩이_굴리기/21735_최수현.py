# 31256 KB, 44 ms
import sys
input = sys.stdin.readline

def roll(snow_ball, check, index):
    # m번 굴렸거나 인덱스 벗어나면 리스트에 추가 후 리턴
    if sum(check) == m or index >= l:
        size.append(snow_ball)
        return
    
    # 방문처리
    check[index] = True
    roll(snow_ball + snow[index], check, index + 1)   # +1칸으로 굴리는 경우
    roll((snow_ball + snow[index])//2, check, index + 2)  # +2칸으로 굴리는 경우
    check[index] = False


n, m = map(int, input().split())
snow = list(map(int, input().split()))

if n <= m:
    print(sum(snow) + 1)
else:
    l = min(m * 2, n)  # 눈덩이 굴리기가 끝날 수 밖에 없는 지점
    visited = [False] * l
    size = []

    # 현재 눈덩이 크기, 방문리스트, 방문할 인덱스
    roll(1, visited, 0)
    roll(0, visited, 1) # 0을 건너뛰고 1로 가면 현재 눈덩이가 절반 감소하므로 0으로 시작

    print(max(size))