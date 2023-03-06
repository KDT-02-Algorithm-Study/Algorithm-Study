N = int(input())
d = 2
while d <= N:
    if N % d == 0:
        print(d)
        N /= d
    else:
        d += 1