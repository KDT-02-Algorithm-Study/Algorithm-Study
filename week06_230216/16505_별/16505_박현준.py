def pprint(lst):
    m = 2**N
    for i in range(m):
        for j in range(m-i):
            print(lst[i][j], end='')
        print()

def triangle(N, x, y):
    if N == 0:
        lst[x][y] = '*'
        return    
    triangle(N-1, x, y)
    triangle(N-1, x + 2**(N-1), y)
    triangle(N-1, x, y + 2**(N-1))    

N = int(input())

lst = [[' '] * (2**N) for _ in range(2**N)]

triangle(N, 0, 0)

pprint(lst)