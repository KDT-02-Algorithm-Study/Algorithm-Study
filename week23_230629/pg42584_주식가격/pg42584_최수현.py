def solution(prices):
    answer = [0] * len(prices)
    stack = [] # 오름차순 stack
    
    for i in range(len(prices)):
        # 현재 stack에 있는 인덱스 모두 +1
        for v, j in stack:
            answer[j] += 1
        
        # stack이 오름차순으로 유지되도록
        while stack and stack[-1][0] > prices[i]:
            stack.pop()
        stack.append((prices[i], i))
    
    return answer