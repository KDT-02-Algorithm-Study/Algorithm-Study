# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/176962

# 시간을 분 단위로 바꿔주는 함수
def time_converter(s):
    h, m = map(int, s.split(':'))

    return h * 60 + m


def solution(plans):
    for plan in plans:
        plan[1] = time_converter(plan[1])
        plan[2] = int(plan[2])

    # 시작 시간이 빠른 순으로 정렬
    plans = sorted(plans, key=lambda x: x[1])
    answer = []
    # 현재 진행중인 과제를 저장할 리스트
    # 중간에 멈춘 과제들도 함께 저장되기 때문에 마지막 과제가 현재 해야하는 과제임
    works = []
    now = plans[0][1] # 현재 시간
    idx = 0

    while idx < len(plans):
        works.append(plans[idx])

        # 현재 시간에 해야할 과제가 없으면 다음 과제 시간으로 초기화
        # ex) 현재 시간 12:50 다음 과제 시간 15:00일 때 현재 시간을 15:00으로 초기화
        if now < works[-1][1]:
            now = works[-1][1]

        while works:
            # 현재 해야하는 과제를 마쳤으면 다음 과제로 넘어가기 위해 break
            if works[-1][2] == 0:
                break
            
            # 현재 과제를 진행 중이므로 현재 시간은 + 1 playtime은 - 1
            now += 1
            works[-1][2] -= 1

            # 과제를 마쳤으면 answer에 저장하고 works에서 제거
            if works[-1][2] == 0:
                answer.append(works.pop()[0])

            # 다음 과제를 진행해야할 시간이 되면 새로운 과제를 시작해야 함
            # 새로운 과제를 works에 저장
            if idx+1 < len(plans) and now == plans[idx+1][1]:
                works.append(plans[idx+1])
                idx += 1

        idx += 1
    
    return answer


'''
  now	     works                                                                                 answer
"12:20"	  ["music", "12:20", "40"]
"12:30"	  ["music", "12:20", "30"], ["computer", "12:30", "100"]
"12:40"	  ["music", "12:20", "30"], ["computer", "12:30", "90"], ["science", "12:40", "50"]
"13:30"	  ["music", "12:20", "30"], ["computer", "12:30", "90"]                                  ["science"]
"14:00"	  ["music", "12:20", "30"], ["computer", "12:30", "60"], ["history", "14:00", "30"]
"14:30"	  ["music", "12:20", "30"], ["computer", "12:30", "60"]                                  ["science", "history"]
"15:30"	  ["music", "12:20", "30"]                                                               ["science", "history", "computer"]
"16:00"	                                                                                         ["science", "history", "computer", "music"]
'''