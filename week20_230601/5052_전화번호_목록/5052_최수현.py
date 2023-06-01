# 31256 KB / 48 ms
import sys
input = sys.stdin.readline

turn = 0
while 1:
    turn += 1
    S = input().rstrip()
    if S[0] == '-':
        break
    
    stack = []
    cnt = 0
    for s in S:
        # 시작 괄호면 무조건 append
        if s == '{':
            stack.append(s)
        else:
            # 닫는 괄호인 경우 stack에 열린괄호 존재하면 pop
            if stack:
                stack.pop()
            # stack 비어있으면 닫힌 괄호를 바꿔야하므로 cnt+1하고 append
            else:
                cnt += 1
                stack.append('{')
    
    # 바꾼 괄호 수 + 바꿔야할 괄호 수(stack의 절반)
    ans = cnt + len(stack)//2
    print(f'{turn}. {ans}')