from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    for _ in range(len(prices)):
        price = prices.popleft()
        tmp = 0
        
        for i in prices:
            tmp += 1
            if price > i:
                break
        answer.append(tmp)
    return answer