def solution(number, k):
    check = [False] * len(number)
    stack = [(number[0], 0)]
    is_end = False
    
    for i in range(1, len(number)):
        if number[i] > stack[-1][0]:
            while stack and stack[-1][0] < number[i]:
                n, index = stack.pop()
                check[index] = True
                k -= 1
                if k == 0:
                    is_end = True
                    break
            if is_end:
                break
        stack.append((number[i], i))
    # 한바퀴 돌았는데 k가 0이 아닐때
    else:
        for i in reversed(range(len(number))):
            if not check[i]:
                check[i] = True
                k -= 1
                if k == 0:
                    break

    ans = ''
    for i in range(len(number)):
        if not check[i]:
            ans += number[i]
    
    return ans