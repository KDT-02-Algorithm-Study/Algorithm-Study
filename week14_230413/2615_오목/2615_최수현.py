# 31256 KB / 44 ms
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def explore():
    for y in range(19):
        for x in range(19):
            if omok[y][x] != 0:
                # 가로
                cnt1 = cnt2 = 0
                # ←
                for i in range(1, 19):
                    if (x - i) < 0 or omok[y][x-i] != omok[y][x]:
                        break
                    else:
                        cnt1 += 1
                # →
                for i in range(1, 19):
                    if (x + i) > 18 or omok[y][x+i] != omok[y][x]:
                        break
                    else:
                        cnt2 += 1
                
                if cnt1 + cnt2 + 1 == 5:
                    print(omok[y][x])
                    print(y + 1, x - cnt1 + 1)
                    return

                # 세로
                cnt1 = cnt2 = 0
                # ↑
                for i in range(1, 19):
                    if (y - i) < 0 or omok[y-i][x] != omok[y][x]:
                        break
                    else:
                        cnt1 += 1
                # ↓
                for i in range(1, 19):
                    if (y + i) > 18 or omok[y+i][x] != omok[y][x]:
                        break
                    else:
                        cnt2 += 1
                
                if cnt1 + cnt2 + 1 == 5:
                    print(omok[y][x])
                    print(y - cnt1 + 1, x + 1)
                    return

                # 대각선1
                cnt1 = cnt2 = 0
                # ↖
                for i in range(1, 19):
                    if (y - i) < 0 or (x - i) < 0 or omok[y-i][x-i] != omok[y][x]:
                        break
                    else:
                        cnt1 += 1
                # ↘
                for i in range(1, 19):
                    if (y + i) > 18 or (x + i) > 18 or omok[y+i][x+i] != omok[y][x]:
                        break
                    else:
                        cnt2 += 1
                
                if cnt1 + cnt2 + 1 == 5:
                    print(omok[y][x])
                    print(y - cnt1 + 1, x - cnt1 + 1)
                    return

                # 대각선2
                cnt1 = cnt2 = 0
                # ↗
                for i in range(1, 19):
                    if (y - i) < 0 or (x + i) > 18 or omok[y-i][x+i] != omok[y][x]:
                        break
                    else:
                        cnt1 += 1
                # ↙
                for i in range(1, 19):
                    if (y + i) > 18 or (x - i) < 0 or omok[y+i][x-i] != omok[y][x]:
                        break
                    else:
                        cnt2 += 1
                
                if cnt1 + cnt2 + 1 == 5:
                    print(omok[y][x])
                    print(y + cnt2 + 1, x - cnt2 + 1)
                    return
    return print(0)

omok = [list(map(int, input().split())) for _ in range(19)]
explore()