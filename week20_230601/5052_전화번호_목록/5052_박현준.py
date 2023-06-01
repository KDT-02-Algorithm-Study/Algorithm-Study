# 32276 KB / 172 ms

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    phone = sorted([input().rstrip() for _ in range(N)])
    for i in range(N-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            print('NO')
            break
    else:
        print('YES')