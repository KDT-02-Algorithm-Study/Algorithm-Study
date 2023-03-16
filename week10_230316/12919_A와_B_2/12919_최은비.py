# 12919 A와 B 2 https://www.acmicpc.net/problem/12919
# 31256KB / 40ms
# T에서 S를 만들 수 있는지를 확인

import sys
input = sys.stdin.readline

def game(s):
    global zero

    if len(s) == len(S):
        if s == S:
            zero = True
        return
    
    # 문자열이 B로 시작하면 뒤집고 B를 삭제한 다음에 재귀
    if s[0] == 'B':
        tmp = s[::-1]
        tmp = tmp[:-1]
        game(tmp)

    # 문자열이 A로 끝나면 A를 삭제한 문자로 다시 재귀
    if s[-1] == 'A':
        tmp = s[:-1]
        game(tmp)
        

S = input().strip()
T = input().strip()
zero = False

game(T)

if zero:
    print(1)
else:
    print(0)


'''
재귀 없이

S = input().strip()
T = input().strip()
zero = False
tmp = []
tmp.append(T)

while tmp:
    s = tmp.pop(0)

    if s == S:
        zero = True
        break

    if len(s) < len(S):
        zero = False
        break

    if s[0] == 'B':
        tmp.append(s[::-1][:-1])

    if s[-1] == 'A':
        tmp.append(s[:-1])

if zero:
    print(1)
else:
    print(0)
'''
