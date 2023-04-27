# 2504 괄호의 값
# 31256 KB / 44 ms

def check1():
    r = 0
    while d and f[0]:
        b = d.pop()
        if b == '(':
            r += check1()
        elif b == '[':
            r += check2()
        elif b == ')':
            return 2*max(1, r)
        else:
            f[0] = 0
            break
    return 0

def check2():
    r = 0
    while d and f[0]:
        c = d.pop()
        if c == '(':
            r += check1()
        elif c == '[':
            r += check2()
        elif c == ']':
            return 3*max(1, r)
        else:
            f[0] = 0
            break
    return 0

d = list(input())[::-1]
f = [1]
result = 0
while d and f[0]:
    a = d.pop()
    if a == '(':
        result += check1()
    elif a == '[':
        result += check2()
    else:
        f[0] = 0
        break
if f[0]:
    print(result)
else:
    print(0)




# 재귀 하나로 합친 방법
'''
import sys

s = list(input())[::-1]
def check(c):
    r = 0
    while s:
        a = s.pop()
        if a == '(' or a == '[':
            r += check(a)
        elif c == '(' and a == ')':
            return 2*max(1, r)
        elif c == '[' and a == ']':
            return 3*max(1, r)
    print(0)
    sys.exit()
answer = 0
while s:
    answer += check(s.pop())
print(answer)
'''