# 프로그래머스 42885 구명보트

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))      # 정렬해서 deque에 담음

    while people:                       # 모든 인원이 빠질 때까지
        person = people.pop()           # 제일 무거운 인원을 태움
        # 현재 인원에서 제일 가벼운 인원을 같이 태울 수 있으면
        if len(people) > 0 and person + people[0] <= limit:
            people.popleft()            # 그 인원도 태움
        answer += 1                     # 보트 + 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (1.97ms, 10.3MB)
# 테스트 2 〉	통과 (0.98ms, 10.2MB)
# 테스트 3 〉	통과 (1.58ms, 10.1MB)
# 테스트 4 〉	통과 (1.24ms, 10.1MB)
# 테스트 5 〉	통과 (0.69ms, 10.2MB)
# 테스트 6 〉	통과 (0.41ms, 10.1MB)
# 테스트 7 〉	통과 (0.66ms, 10.3MB)
# 테스트 8 〉	통과 (0.08ms, 10.2MB)
# 테스트 9 〉	통과 (0.12ms, 10.2MB)
# 테스트 10 〉	통과 (0.73ms, 10.4MB)
# 테스트 11 〉	통과 (0.76ms, 10.3MB)
# 테스트 12 〉	통과 (0.57ms, 10.2MB)
# 테스트 13 〉	통과 (1.23ms, 10.2MB)
# 테스트 14 〉	통과 (0.97ms, 10.2MB)
# 테스트 15 〉	통과 (0.14ms, 10.1MB)

# 효율성  테스트
# 테스트 1 〉	통과 (11.20ms, 11MB)
# 테스트 2 〉	통과 (11.78ms, 11MB)
# 테스트 3 〉	통과 (10.42ms, 11.1MB)
# 테스트 4 〉	통과 (13.13ms, 11.1MB)
# 테스트 5 〉	통과 (11.18ms, 11MB)