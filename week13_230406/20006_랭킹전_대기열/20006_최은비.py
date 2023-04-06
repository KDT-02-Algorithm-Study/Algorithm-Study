# 랭킹전 대기열 https://www.acmicpc.net/problem/20006
# 31256KB / 44ms
import sys
from collections import deque
input = sys.stdin.readline

p, m = map(int, input().split())
player = [] # 입력으로 들어오는 플레이어 정보
game = [] # 게임방 정보
# game 리스트는 첫 번째로 들어오는 플레이어의 레벨을 기준으로 잡아야 하니까
# game = [[player_lv, [(lv, name), (lv, name)]], [player_lv, [(lv, name), (lv, name)]], ...] 와 같은 형태로 값을 삽입시켜야 함

for _ in range(p):
    a, b = input().split()
    player.append((int(a), b))

for lv, name in player:
    # 해당 플레이어의 입장 여부
    flag = False

    for i in range(len(game)):
        # 현재 방 인원이 모두 찼으면 pass
        if len(game[i][1]) == m:
            continue
        
        # 어느 방에도 들어가지 않았고, 레벨 기준에 부합하면 입장
        if not flag and game[i][0] - 10 <= lv and game[i][0] + 10 >= lv:
            flag = True
            game[i][1].append((lv, name))

    # 어느 방과도 매칭이 안 되면 방을 새로 만들기
    if not flag:
        game.append([lv, [(lv, name)]])

for i in range(len(game)):
    if len(game[i][1]) == m:
        print('Started!')
    else:
        print('Waiting!')

    tmp = sorted(game[i][1], key=lambda x: x[1])
    for j in range(len(tmp)):
        print(*tmp[j])