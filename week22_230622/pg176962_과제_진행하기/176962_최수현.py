def solution(plans):
    plans.sort(key=lambda x: x[1]) # 시작시간 순 정렬
    uncomplete = []
    answer = []
    i = 0

    # 범위를 마지막 과제 전까지 잡음
    while i < len(plans)-1:
        name, start, running_time = plans[i]
        # 시간 계산 & 형변환
        s = int(start[:2]) * 60 + int(start[-2:])
        next_s = int(plans[i+1][1][:2]) * 60 + int(plans[i+1][1][-2:])
        running_time = int(running_time)
        gap = next_s - s

        # 다음 과제까지 시간이 넉넉하면 현재 과제 완료 & 못끝낸 과제 하기
        if gap >= running_time:
            answer.append(name)
            gap -= running_time
            # 남은 시간에 따라 못했던 과제 완료 or 시간 빼기
            while uncomplete and gap > 0:
                n, t = uncomplete.pop()
                if t <= gap:
                    answer.append(n)
                    gap -= t
                else:
                    uncomplete.append([n, t-gap])
                    break
        # 다 못끝내면 시간 빼고 uncomplete에 추가
        else:
            uncomplete.append([name, running_time-gap])
        i+= 1

    # 마지막 과제 완료하고 못끝낸 과제 뒤에서부터 answer에 추가
    answer.append(plans[-1][0])
    while uncomplete:
        answer.append(uncomplete.pop()[0])

    return answer