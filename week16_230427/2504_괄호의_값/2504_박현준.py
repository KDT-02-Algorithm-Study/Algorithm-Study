# 31388 KB / 44 ms

lst = [x for x in input()]
stack = []

# 소괄호 값
value_sm = 2

# 대괄호 값
value_lg = 3

# 값을 곱하는 과정을 담는 변수
tmp = 1

# 최종 답
res = 0
for i in range(len(lst)):
    # 괄호
    b = lst[i]
    
    # 괄호가 '(' or '[' 일 때, stack에 추가해주고 동시에 값을 tmp에 저장
    if b == '(':
        tmp *= value_sm
        stack.append(b)
    elif b == '[':
        tmp *= value_lg
        stack.append(b)
    
    # ')' 일 때 짝이 맞으면
    elif b == ')':
        
        # 스택이 비었거나 짝이 아니면 break
        if not stack or stack[-1] == '[':
            res = 0
            break
        
        else:
        # 짝이 맞으면 곱해줬던 tmp를 res에 더해주고 tmp를 이전 상태로 돌림
            if lst[i-1] == '(':
                res += tmp
            tmp //= value_sm
            stack.pop()
        
    # ']' 일 때 짝이 맞으면
    elif b == ']':
        
        # 스택이 비었거나 짝이 아니면 break 
        if not stack or stack[-1] == '(':
            res = 0
            break
        
        else:
            
            # 짝이 맞으면 곱해줬던 tmp를 res에 더해주고 tmp를 이전 상태로 돌림
            if lst[i-1] == '[':
                res += tmp
            tmp //= value_lg
            stack.pop()
            
if stack:
    print(0)
else:
    print(res)

    """
    
    """

