# 전화번호 목록 https://www.acmicpc.net/problem/5052
# 32276KB / 172ms
import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    phone = [input().strip() for _ in range(n)]

    phone.sort()
    
    for i in range(n-1):
        l = len(phone[i])
        if phone[i] == phone[i+1][:l]:
            print("NO")
            break
    else:
        print("YES")