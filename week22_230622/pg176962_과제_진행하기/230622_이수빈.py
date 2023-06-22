def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        start_time = h*60+m
        plans[i][1] = start_time
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x:x[1]) # 랜덤으로 들어오니까 정렬
    start_timeack = []

    # 시간안에 과제를 못 끝낼경우와 끝낼경우
    for i in range(len(plans)): 
        if i == len(plans)-1: 
            start_timeack.append(plans[i])
            break
        
        # 다음 시작 시간
        sub, start_time, t = plans[i]
        nsub, nstart_time, nt = plans[i+1]

        # 진행중이던 과제가 시간 내에 완료할 경우 
        if start_time + t <= nstart_time:
            answer.append(sub)
            temp_time = nstart_time - (start_time+t) # 남은 시간은 감소
            
            # 진행중이던 과제를 하고 나서도 시간이 남을 경우
            while temp_time != 0 and start_timeack:
                tsub, tstart_time, tt = start_timeack.pop() # 가장 최근에 한 애를 가져옴 
                if temp_time >= tt: # 과제 완료했을 경우 
                    answer.append(tsub) #  리스트에 추가 
                    temp_time -= tt
                else: # 완료 못했을 경우 잔여 시간을 추가 
                    start_timeack.append([tsub, tstart_time, tt - temp_time])
                    temp_time = 0
            
        else: # 진행중이던 과제를 시간 내 완료를 못 한 경우 
            plans[i][2] = t - (nstart_time - start_time)
            start_timeack.append(plans[i])
        
    while start_timeack:
        sub, start_time, tt = start_timeack.pop()
        answer.append(sub) 
    
    # 남은 과제가 있으면.. 마지막 원소부터 
    return answer