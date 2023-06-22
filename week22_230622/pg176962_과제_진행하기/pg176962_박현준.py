def solution(plans):
    answer = []
    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(':'))
        plans[i][1] = hour * 60 + minute
        plans[i][2] = int(plans[i][2])

    plans = sorted(plans, key=lambda x:x[1])
    pause_plans = []
    
    for i in range(len(plans)):
        if i == len(plans)-1:
            pause_plans.append(plans[i])
            break
        name, start, time = plans[i][0], plans[i][1], plans[i][2]
        next_name, next_start, next_time = plans[i+1][0], plans[i+1][1], plans[i+1][2]
        
        if start + time <= next_start:
            answer.append(name)
            temp = next_start - (start + time)
            
            while temp != 0 and pause_plans:
                pause_name, pause_start, pause_time = pause_plans.pop()
                if temp >= pause_time:
                    answer.append(pause_name)
                    temp -= pause_time
                else:
                    pause_plans.append([pause_name, pause_start, pause_time - temp])
                    temp = 0
        else:
            plans[i][2] = time - (next_start - start)
            pause_plans.append(plans[i])
    while pause_plans:
        name, start, pause_time = pause_plans.pop()
        answer.append(name)
    return answer