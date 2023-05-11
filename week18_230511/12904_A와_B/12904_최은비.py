# A와 B https://www.acmicpc.net/problem/12904
# 31256KB / 44ms
import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

while True:
    # 문자열 마지막이 A면 마지막 문자를 뺀다
    if t[-1] == 'A':
        t = t[:-1]
        
    # 문자열 마지막이 B면 마지막 문자를 빼고 뒤집는다
    else:
        t = t[:-1]
        t = t[::-1]

    # s와 같아지거나 t의 길이가 1이 되면 반복문을 종료
    if t == s or len(t) == 1:
        break

if s == t:
    print(1)
else:
    print(0)