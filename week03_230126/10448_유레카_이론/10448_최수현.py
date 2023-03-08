import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    tri = []
    tri_n = 1
    grow_n = 2
    while tri_n < n:
        tri.append(tri_n)
        tri_n += grow_n
        grow_n += 1
    
    result = 0
    for i in tri:
        for j in tri:
            for k in tri:
                if i+j+k == n:
                    result = 1
                    break
            if result == 1:
                break
        if result == 1:
            break
    print(result)