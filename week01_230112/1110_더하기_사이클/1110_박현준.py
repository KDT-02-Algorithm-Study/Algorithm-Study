N = int(input())
_N = N
cnt = tmp = 0
while 1:
    tail = _N % 10
    head = _N // 10
    tmp = tail + head
    if tmp >= 10:
        tmp %= 10
    _N = tail*10 + tmp
    cnt += 1
    if _N == N:
        break
print(cnt)