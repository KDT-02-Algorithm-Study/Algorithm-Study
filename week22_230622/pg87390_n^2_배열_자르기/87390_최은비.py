# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n ,left, right):
    answer = []

    for i in range(left, right+1):
        x = i // n
        y = i % n
        answer.append(max(x, y) + 1)

    return answer


'''
n = 3

 좌표     값
(0, 0)    1
(0, 1)    2
(0, 2)    3
(1, 0)    2
(1, 1)    2
(1, 2)    3
(2, 0)    3
(2, 1)    3
(2, 2)    3

-> 값 = max(x, y) + 1
'''