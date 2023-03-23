# 31388 KB / 64 ms

N = int(input())
A = [int(x) for x in input().split()]
plus, minus, mul, div = map(int, input().split())
mxm = -999999999999999
mnm = 99999999999999999

def back(depth, total, index, plus, minus, mul, div):
    global mxm
    global mnm
    if depth == N-1:
        mxm = max(mxm, total)
        mnm = min(mnm, total)
        return
    # 더하기
    if plus:
        back(depth+1, total + A[index], index+1, plus-1, minus, mul, div)
    # 빼기
    if minus:
        back(depth+1, total - A[index], index+1, plus, minus-1, mul, div)
    # 곱하기
    if mul:
        back(depth+1, total * A[index], index+1, plus, minus, mul-1, div)
    # 빼기
    if div:
        back(depth+1, int(total / A[index]), index+1, plus, minus, mul, div-1)

back(0, A[0], 1, plus, minus, mul, div)

print(mxm, mnm, sep='\n')