# 171256 KB / 3776 ms 

T = int(input())
for _ in range(T):
    N = int(input())
    stocks = [int(x) for x in input().split()]
    mxm = stocks[-1]
    res = 0
    for i in range(N-1, -1, -1):
        if mxm < stocks[i]:
            mxm = stocks[i]
        res += mxm - stocks[i]
    print(res)