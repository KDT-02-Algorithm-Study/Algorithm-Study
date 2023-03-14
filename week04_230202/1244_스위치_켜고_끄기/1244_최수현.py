import sys
input = sys.stdin.readline

n = int(input())
on_off = list(map(int, input().split()))

m = int(input())
for i in range(m):
    gender, switch = map(int, input().split())
    if gender == 1:
        s = switch
        while switch <= len(on_off):
            on_off[switch-1] ^= 1
            switch += s
    else:
        on_off[switch-1] ^= 1
        a = b = switch-1
        while a-1 >= 0 and b+1 < n:
            if on_off[a-1] == on_off[b+1]:
                a -= 1
                b += 1
                on_off[a] ^= 1
                on_off[b] ^= 1
            else:
                break
for i in range(n):
    print(on_off[i], end=' ')
    if i % 20 == 19:
        print()