from collections import deque

def solution(queue1, queue2):
    count = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    while True:
        if count == (len(queue1) + len(queue2)) * 2:
            return -1
        
        if sum1 == sum2:
            return count
        
        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num

        count += 1