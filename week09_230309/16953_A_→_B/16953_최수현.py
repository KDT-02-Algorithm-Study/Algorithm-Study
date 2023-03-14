# 메모리 31256 KB, 시간 40 ms
a, b = map(int, input().split())
cnt = 0

while b > a:
    if b & 1:
        if b % 10 == 1:
            b //= 10
        else:
            break
    else:
        b //= 2
    
    cnt += 1

print(cnt + 1 if a == b else -1)