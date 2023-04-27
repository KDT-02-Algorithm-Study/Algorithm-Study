# 괄호의 값 https://www.acmicpc.net/problem/2504
# 31388KB / 40ms
import sys
input = sys.stdin.readline

'''
str: (  (  )  [  [   ]   ]   )   (   [   ]   )
tmp: 2  4  2  6  18  6   2   1   2   6   2   1
ans: 0  0  4  4  4   22  22  22  22  22  28  28
'''

string = list(input().strip())
stack = []
tmp = 1
ans = 0

for i in range(len(string)):
    if string[i] == '(':
        tmp *= 2
        stack.append(string[i])
    elif string[i] == '[':
        tmp *= 3
        stack.append(string[i])

    if string[i] == ')':
        if stack:
            k = stack.pop()
            # 짝이 맞지 않으면 반복문 탈출
            if k != '(':
                ans = 0
                break
            else:
                # 짝이 맞더라도 직전에 괄호값과 일치할 때만 결과에 더해줘야 함
                if string[i-1] == '(':
                    ans += tmp
                tmp //= 2
        # 스택이 비어있으면 올바르지 않은 괄호임 > 반복문 탈출
        else:
            ans = 0
            break
    
    # 위 로직 반복
    elif string[i] == ']':
        if stack:
            k = stack.pop()
            if k != '[':
                ans = 0
                break
            else:
                if string[i-1] == '[':
                    ans += tmp
                tmp //= 3
        else:
            ans = 0
            break

if stack:
    ans = 0

print(ans)