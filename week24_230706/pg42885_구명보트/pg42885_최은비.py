# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    # 무게순으로 정렬
    people = deque(sorted(people))
    
    while people:
        if len(people) > 1:
            # 가장 무거운 사람과 가장 가벼운 사람을 태웠을 때 무게 제한을 넘으면
            # 가장 무거운 사람만 보내기
            if people[0] + people[-1] > limit:
                people.pop()

            # 제한을 넘지 않으면 둘 다 태우기
            else:
                people.popleft()
                people.pop()

        else:
            people.pop()
            
        answer += 1
    
    return answer