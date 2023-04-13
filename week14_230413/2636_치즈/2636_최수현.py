# 31256 KB / 44 ms
import sys
input = sys.stdin.readline

# 1. 탐색한 지점에 연결된 0(접근가능한 모든 공기)은 모두 True처리하기
# 2. True처리가 된 지점과 바로 붙어있는 1(치즈)을 녹이기


# melting = 탐색할 좌표 리스트, turn = 시간
def melt(melting, turn):
    # 현재 단계에서 녹는 치즈의 수 저장
    result = len(melting)
    # 다음 단계에서 녹을 치즈 좌표 저장
    new_melting = []

    while melting:
        y, x = melting.pop()
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if ny >= 0 and ny < r and nx >= 0 and nx < c:
                if not check[ny][nx]:
                    # 방문처리
                    check[ny][nx] = True
                    # 0인 경우 계속 탐색을 위해 melting에 추가
                    if cheese[ny][nx] == 0:
                        melting.append((ny, nx))
                    # 1인 경우 new_melting에 추가
                    else:
                        new_melting.append((ny, nx))

    if new_melting:
        return melt(new_melting, turn + 1)
    # 다음 턴에 녹일 치즈가 없다면(다 녹았다면) 시간과 치즈수 return
    else:
        return turn, result


r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(r)]
check = [[False] * c for _ in range(r)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# (0, 0)에서 시작할거라 True로 탐색 바꾸고 시작
check[0][0] = True
print(*melt([(0, 0)], 0), sep='\n')