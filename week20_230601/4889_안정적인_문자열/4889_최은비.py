# 안정적인 문자열 https://www.acmicpc.net/problem/4889
# 31256KB / 48ms

import sys
input = sys.stdin.readline

def check(stack, cnt):
    now_cnt = cnt
    tmp = []
    
    for i in stack:
        if not tmp:
            # 비교할 괄호가 없는데 닫는 괄호가 입력되면 수행 횟수 + 1 하고 여는 괄호로 바꿔서 append
            if i == '}':
                now_cnt += 1
                tmp.append('{')
            # 여는 괄호는 바로 append
            else:
                tmp.append(i)
        else:
            # 마지막 괄호와 다음 괄호가 같으면 수행횟수 + 1 하고 pop
            if tmp[-1] == '{':
                if i == '{':
                    now_cnt += 1
                tmp.pop()
            else:
                if i == '}':
                    now_cnt += 1
                tmp.pop()

    # 짝이 맞지 않아서 남는 괄호가 있으면 재귀
    if tmp:
        check(tmp, now_cnt)
    else:
        return now_cnt
        
test = 0
while True:
    s = input().strip()
    stack = []
    ans = 0

    # - 가 입력되면 종료
    if s[0] == '-':
        break

    # 처음 입력이 안정적인 문자열인지 확인
    for i in s:
        # stack에 괄호가 하나 이상 있고, 짝이 맞으면 pop
        if stack and i == '}' and stack[-1] == '{':
            stack.pop()
        # 아니면 append
        else:
            stack.append(i)

    # 안정적인 문자열이 아니면 남은 괄호로 함수 실행
    if stack:
        ans = check(stack, 0)
        
    test += 1
    print(f"{test}. {ans}")