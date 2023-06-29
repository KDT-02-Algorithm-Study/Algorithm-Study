# 프로그래머스 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_que1 = sum(queue1)
    sum_que2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    # 최대 실행 횟수 : queue1에 있는 모든 원소를 queue2로 옮기고 다시 queue1으로 옮긴 횟수 == queue1 길이의 3배
    max_cnt = len(queue1) * 3
    
    # 전체 합이 홀수면 절대 같은 값으로 만들 수 없음
    if (sum_que1 + sum_que2) // 2 == 1:
        answer = -1
        return answer
    
    # 실행 횟수를 count하는 변수
    cnt = 0
    while cnt < max_cnt:
        if sum_que1 == sum_que2:
            break
        
        if sum_que1 > sum_que2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            answer += 1
            # 매 반복마다 sum()을 실행하면 시간초과
            sum_que1 -= tmp
            sum_que2 += tmp
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            answer += 1
            sum_que2 -= tmp
            sum_que1 += tmp
            
        cnt += 1
        
    if cnt >= max_cnt:
        answer = -1
    
    return answer