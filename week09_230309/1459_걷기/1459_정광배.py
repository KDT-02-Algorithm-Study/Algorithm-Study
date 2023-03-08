# 1459 걷기
# 31256 KB / 44 ms

# (x, y)집, 우하, 대각
x, y, w, s = map(int, input().split())

# w*2가 대각보다 빠르거나 같을 경우
if 2*w <= s:
    result = (x+y)*w
# 대각이 빠를 경우
elif w > s:
    min_ = min(x, y)
    t = abs(x - y)
    if t & 1:   # 남은게 홀수
        result = (min_+t-1)*s+w
    else:       # 남은게 짝수
        result = (min_+t)*s
# w*2 > s >= w
else:
    min_ = min(x, y)
    t = abs(x - y)
    result = (min_)*s+t*w
print(result)