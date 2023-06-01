# 31256 KB / 52 ms

T = 1
while True:
    count = 0
    S = input()
    S_length = len(S)
    if S.count('-') > 0:
        break
    
    stack = []
    for i in S:
        if i == '{':
            stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                count += 1
                stack.append('{')
    res = len(stack) // 2 + count
    print(f'{T}. {res}')
    T += 1