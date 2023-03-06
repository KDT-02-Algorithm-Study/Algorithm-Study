# https://www.acmicpc.net/problem/10448

import sys
input = sys.stdin.readline

test = int(input())

tri = [(i*(i+1)//2) for i in range(1, 45)]

for i in range(test):
    num = int(input())
    total = 0
    is_three = False

    for a in range(len(tri)):
        for b in range(len(tri)):
            for c in range(len(tri)):
                total = tri[a] + tri[b] + tri[c]
                if total == num:
                    is_three = True
                    break
            if total == num:
                break
        if total == num:
            break
    
    print(int(is_three))