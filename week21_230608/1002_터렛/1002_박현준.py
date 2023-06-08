import math
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 중심의 거리
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    # 중심이 같음
    if distance == 0:
        if r1 == r2:
            res = -1
        else:
            res = 0
    
    # 중심이 다름
    else:
        if distance < r1 + r2 and abs(r1 - r2) < distance:
            res = 2
        elif distance == r1 + r2 or abs(r1- r2) == distance:
            res = 1
        else:
            res = 0
    print(res)