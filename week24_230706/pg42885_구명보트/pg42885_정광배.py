# 구명보트
# 테스트 2 〉	통과 (10.06ms, 10.6MB)

def solution(people, limit):
    answer = 0
    people.sort()
    
    s = 0
    e = len(people) - 1
    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
        answer += 1
        e -= 1
    return answer