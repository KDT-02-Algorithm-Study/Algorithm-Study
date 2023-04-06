# 4659 비밀번호 발음하기
# 31256 KB / 40 ms

import sys
input = sys.stdin.readline

s = ('a', 'e', 'i', 'o', 'u')
while True:
    a = input().rstrip()
    if a == 'end':
        break
    f = 1
    if not any(i in a for i in s):
        f = 0
    for j in range(len(a)-2):
        if all(a[j+n] in s for n in range(3)):
            f = 0
        if all(a[j+m] not in s for m in range(3)):
            f = 0

    for k in range(len(a)-1):
        if a[k] not in ('e','o'):
            if a[k] == a[k+1]:
                f = 0
    if f:
        print(f'<{a}> is acceptable.')
    else:
        print(f'<{a}> is not acceptable.')