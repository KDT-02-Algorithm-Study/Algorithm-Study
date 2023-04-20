# 14891 톱니바퀴
# 34160 KB / 64 ms 
# 기본 코드
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 맞닿은 극이 다르다면, 전 톱니와 반대방향으로 회전
# 맞닿은 극이 같으면, 회전하지 않음
# 옆에 톱니바퀴가 회전하지 않으면 회전하지 않음


def rotate_right(x, d):
    if x > 4 or gears[x - 1][2] == gears[x][6]:
        return

    if gears[x - 1][2] != gears[x][6]:
        rotate_right(x + 1, -d)
        gears[x].rotate(d)

 
def rotate_left(x, d):
    if x < 1 or gears[x][2] == gears[x + 1][6]:
        return

    if gears[x][2] != gears[x + 1][6]:
        rotate_left(x - 1, -d)
        gears[x].rotate(d)

 
gears = {}
for i in range(1, 5):
    gears[i] = deque((map(int, input().rstrip())))
k = int(input())
for _ in range(k):
    x, d = map(int, input().split())

    rotate_right(x + 1, -d)
    rotate_left(x - 1, -d)
    gears[x].rotate(d)

ans = 0
for i in range(4):
    ans += gears[i + 1][0] * (2 ** i)

print(ans)
