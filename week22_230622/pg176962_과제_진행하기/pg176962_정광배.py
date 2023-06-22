# 과제 진행하기
# 테스트 14 〉	통과 (56.06ms, 10.7MB)
# 4, 5, 6, 10, 11, 20 실패ㅠ

def solution(plans):
    answer = []
    plans = sorted(plans, key=lambda x: x[1])
    stack = []
    for i in range(len(plans)):
        a, b, c = plans[i]
        h, m = map(int, b.split(':'))
        s_t = h*60 + m      # 시작 시각(분)
        c = int(c)          # 걸리는 시간
        e_t = s_t + c       # 끝나는 시각
        delay = 0           # 지연된 시간
        if i == 0:          # 처음 과제를 now로 할당
            now = [a, e_t]
            continue
        # 이전 과제가 끝났을 때 (stack 전부를 확인함)
        if s_t >= now[1]:
            answer.append(now[0])       # now를 완료 처리
            while stack:                # stack에 있는 과제들을 확인(선입후출)
                if stack[-1][1] <= s_t:
                    answer.append(stack.pop()[0])
                else:                   # 
                    break
            now = [a, e_t]              # 지금과제를 now로 할당

        # 이전 과제를 멈춰야 할 때
        else:
            delay = c
            # stack에 있는 과제의 끝나는 시간을 delay 시켜줌
            for j in stack:
                j[1] += delay
            stack.append([now[0], now[1]+c])
            now = [a, e_t]

    # now와 stack에 있는 과제를 완료 처리
    answer.append(now[0])
    while stack:
        answer.append(stack.pop()[0])

    return answer