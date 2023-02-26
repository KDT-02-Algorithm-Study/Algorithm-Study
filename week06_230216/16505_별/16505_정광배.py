# 16505 별

def star(n, x, y):
    if n == 1:
        ans[x][y] = '*'
        return
    g = n//2
    star(g, x, y)
    star(g, x+g, y)
    star(g, x, y+g)

N = int(input())
ans = [[' ']*(i+1) for i in reversed(range(2**N))]

if N == 0:
    print('*')
else:
    star(2**N, 0, 0)
    for ele in ans:
        print(''.join(ele))