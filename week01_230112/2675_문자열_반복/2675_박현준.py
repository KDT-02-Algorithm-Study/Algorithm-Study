T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    for i in S:
        print(i*R, end='')
    print()