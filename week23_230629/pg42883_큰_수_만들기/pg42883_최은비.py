# 프로그래머스 큰 수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []
    # 만들어야 하는 문자열의 길이
    ans_len = len(number) - k
    
    for i in range(len(number)):
        # 현재 문자열이 만들어야 하는 문자열의 길이보다 작으면 append
        if len(answer) < ans_len:
            answer.append(number[i])
        
        # 큰 수가 맨 앞에 위치해야 하므로 현재 수보다 다음 수가 크면 계속 pop
        # pop 할 때마다 k에서 1씩 빼주기
        if i+1 < len(number) and int(number[i]) < int(number[i+1]):
            if k > 0:
                while answer and k:
                    # 현재 문자열에 남아 있는 수를 모두 이었을 때 최종 문자열 길이보다 작아지면 안됨
                    if len(answer) + len(number[i:]) <= ans_len:
                        break
                        
                    # 작은 수를 모두 pop 했으면 탈춯
                    if int(answer[-1]) >= int(number[i+1]):
                        break
                        
                    answer.pop()
                    k -= 1

    
    return ''.join(answer)