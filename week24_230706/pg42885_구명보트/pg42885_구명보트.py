# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 0.07ms, 10MB / 1.57ms, 10.3MB (정확성 테스트)
# 11.33ms, 10.7MB / 29.87ms, 10.5MB (효율성 테스트)


'''
# 문제 이해
- 보트는 2명씩만 탈 수 있고, 무게제한이 있음
- 구명 보트를 최대한 적게 사용해서 모든 사람을 구출해야함 

# 문제 해석 
- 최대한 적게 모든 사람 구출  -> "그리디" 활용
- 가장 적은 보트를 사용하려면?  
    : 가장 무거운 사람을 먼저 태우고, 남은 1자리를 제일 가벼운 사람부터  고려해야함 
-> 따라서, "sort와 queue를 활용하여, 가장 많이 나가는 사람과 적게 나가는 사람을 pop하여 계산"

'''
 
from collections import deque

def solution(people, limit):
    boat = 0
    people.sort() # 사람들의 무게를 오름차순 정렬

    q = deque(people)
    while q:
        if len(q) >= 2:
            # 제일 많이 나가는 사람과 적게 나가는 사람을 더해서 limit과  비교 

            if q[0] + q[-1] <= limit: # limit보다 적게 나간다면, 그 두 사람을 pop하고, 보트 수를 하나 증가 
                q.pop() 
                q.popleft()
                boat += 1 # 보트를 타고 나가는 것! 

            elif q[0] + q[-1] > limit: # limit을 초과한다면, 무거운 한 사람만 보트를 타고 나갈 수 있음 
                q.pop()
                boat += 1
        else:
            # 제일 가벼운 사람 한 사람이 남았을 것 
            if q[0] <= limit:
                q.pop()
                boat += 1
    return boat


