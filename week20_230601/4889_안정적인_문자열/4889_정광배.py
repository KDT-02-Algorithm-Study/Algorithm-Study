# 4889 안정적인 문자열
# 31256 KB / 52 ms

import sys
input = sys.stdin.readline

t = 0
while 1:
    t += 1
    
    data = input().rstrip()
    if data[0] == '-':
        break
    
    cnt = 0
    stack = []
    # } 일때 stack의 가장 위가 { 면 바로 pop 해줌
    for i in data:
        if i == '}' and stack and stack[-1] == '{':
                stack.pop()
        else: # 아니면 stack에 추가
            stack.append(i)
    
    # stack 가장 위 2개는 {{, }}, }{ 만 남아있음
    while stack:
        a = stack.pop()
        b = stack.pop()
        if a == b: # {{, }}
            cnt+=1
        else: # }{
            cnt+=2
    print(f'{t}. {cnt}')
