# 1002 터렛
# 31256 KB / 52ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (((x1-x2)**2) + ((y1-y2)**2))**(1/2)

    # 두 원이 동심원, 반지름 같음
    if d == 0 and r1 == r2 :
        print(-1)
    # 내접, 외접일 때
    elif abs(r1-r2) == d or abs(r1+r2) == d: 
        print(1)
    # 두 점에서 만날 때
    elif abs(r1-r2) < d < abs(r1+r2) :
        print(2)
    # 그 외 
    else :
        print(0) 
