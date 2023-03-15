# 메모리 31388 KB, 시간 44 ms
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())

# 0번째에서 시작한다고 생각(1밑에서)
x = 1
y = 0

if k > c * r:
    print(0)
else:
    # 가로로 빼는 것은 한개를 이미 빼고 시작하므로 -1(세로에서 6까지 빼고 7부터 시작)
    c -= 1
    while 1:
        # ↑
        if k - r <= 0:
            y += k
            break
        else:
            k -= r
            y += r
            r -= 1
        
        # →
        if k - c <= 0:
            x += k
            break
        else:
            k -= c
            x += c
            c -= 1

        # ↓
        if k - r <= 0:
            y -= k
            break
        else:
            k -= r
            y -= r
            r -= 1

        # ←
        if k - c <= 0:
            x -= k
            break
        else:
            k -= c
            x -= c
            c -= 1
            
    print(x, y)