def solution(N, left, right):
    answer = []
    for i in range(left, right+1):
        
        row = i // N
        col = i % N
        answer.append(max(row, col) + 1)
    return answer

"""

"""