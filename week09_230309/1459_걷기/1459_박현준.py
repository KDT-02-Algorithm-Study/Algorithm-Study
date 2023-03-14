# 31256 KB / 44 ms

X, Y, W, S = map(int, input().split())

# 평행으로만 움직일 때
parallel = (X + Y) * W

# 대각선으로만 움직일 때 (홀수)
if (X + Y) & 1:
    if X > Y:
        diagnol = (X - 1) * S + W
    else:        
        diagnol = (Y - 1) * S + W
# 대각선으로만 움직일 때 (짝수)
else:
    diagnol = max(X, Y) * S

# 둘 다 있을 때
if X > Y:
    mix = (Y * S) + (X - Y) * W
else:
    mix = (X * S) + (Y - X) * W

# 3가지 방법 중 최솟값을 구한다.
res = min(min(parallel, diagnol), mix)
print(res)