# 16113 시그널
# 31256 KB / 48 ms
# 1등^^

n = int(input())
s = input()
step = n//5 # 한 줄의 길이

ans = ''
i = 0
# 규칙 찾기
while i < step:
    if s[i] == '.':
        i += 1
        continue
    if s[i+3*step] == '#': # 0 1 2 6 8
        if s[i+step] == '.': # 2
            now = '2'
        elif i == step-1: # 1이 마지막 일 때
            ans += '1'
            break
        elif s[i+1] == '.': # 1
            now = '1'
        elif s[i+1+2*step] == '.': # 0
            now = '0'
        elif s[i+2+step] == '.': # 6
            now = '6'
        else: # 8
            now = '8'
    else: # 34579
        if s[i+1] == '.': # 4
            now = '4'
        elif s[i+2*step] == '.': # 7
            now = '7'
        elif s[i+2+step] == '.': # 5
            now = '5'
        elif s[i+step] == '.': # 3
            now = '3'
        else: # 9
            now = '9'

    ans += now

    if now == '1':
        i += 2
    else:
        i += 4

print(ans)
'''
10 8  9
7     7
9  7  9
4     8
8  7  9
'''