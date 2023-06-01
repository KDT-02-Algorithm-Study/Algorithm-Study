# 4889 안정적인 문자열
# 31256KB / 48ms

import sys
input = sys.stdin.readline

i = 0
while 1:
    i += 1
    s = input().rstrip()
    if '-' in s: break

    scount, t = 0, 0
    for st in s:
        if st == '{':           # { 를 만나면 +1
            scount += 1
        else:
            if scount:          # } 를 만났을 때 { 를 만났었다면 -1
                scount -= 1
            else:               # } 를 만났을 때 { 를 
                t += 1
                scount += 1
    print(f'{i}. {t + scount//2}')