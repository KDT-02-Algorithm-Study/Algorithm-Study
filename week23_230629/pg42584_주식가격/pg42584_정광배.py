# 주식가격
# 테스트 3 〉	통과 (28.02ms, 19.5MB)

def solution(data:list):
    l = len(data)
    answer = [0]*l # [0, 0, 0, 0, 0]
    stack = []

    # data를 index와 함께 탐색
    for i, now in enumerate(data):
        # now가 stack 제일 위의 data[index]보다 작으면 pop
        while stack and now < data[stack[-1]]:
            t = stack.pop()
            answer[t] = i-t # (now의 index) - (stack에서 pop했는 index)
        stack.append(i)
        
    # 끝날 때 까지 가격이 떨어지지 않은 경우
    while stack:
        t = stack.pop()
        answer[t] = l-1-t # len - 1 - t
    
    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
            #   0  1  2  3  4


""" 
stack(index)    answer
[]              [0, 0, 0, 0, 0]
[0]             [0, 0, 0, 0, 0]
[0, 1]          [0, 0, 0, 0, 0]
[0, 1, 2]       [0, 0, 0, 0, 0]
[0, 1]          [0, 0, 1, 0, 0]
[0, 1, 3]       [0, 0, 1, 0, 0]
[0, 1, 3, 4]    [0, 0, 1, 0, 0]
[0, 1, 3]       [0, 0, 1, 0, 0]
[0, 1]          [0, 0, 1, 1, 0]
[0]             [0, 3, 1, 1, 0]
[]              [4, 3, 1, 1, 0]
"""