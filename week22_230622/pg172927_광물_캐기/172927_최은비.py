# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/172927

# 가지고 있는 곡괭이 중에서 피로도가 제일 높은 곡괭이로만 작업했을 경우에 피로도를 계산
# 계산한 피로도를 내림차순으로 정렬 -> 높은 피로도 순서대로 좋은 곡괭이로 작업

def solution(picks, minerals):
    # 곡괭이가 하나도 없으면 0 출력
    if sum(picks) == 0:
        return 0
    
    # 가지고 있는 곡괭이 수보다 캐야하는 광물이 많으면 필요한 광물만큼 자르기
    # 가지고 있는 곡괭이 수: 2, 캐야하는 광물: 12 -> 마지막 2개는 작업 못함
    if sum(picks) < len(minerals)/5:
        minerals = minerals[:sum(picks)*5]

    # 하나의 곡괭이로만 작업했을 때 쌓이는 피로도를 저장할 리스트
    hp = [[] for _ in range(len(minerals)//5+1)]
    answer = 0
    
    if picks[2]:
        for i in range(len(minerals)//5+1):
            tmp = 0
            for j in range(i*5, i*5+5):
                if j >= len(minerals):
                    break

                if minerals[j] == 'diamond':
                    tmp += 25
                elif minerals[j] == 'iron':
                    tmp += 5
                else:
                    tmp += 1
            
            hp[i] = [i, tmp]
    
    elif picks[1]:
        for i in range(len(minerals)//5+1):
            tmp = 0
            for j in range(i*5, i*5+5):
                if j >= len(minerals):
                    break

                if minerals[j] == 'diamond':
                    tmp += 5
                else:
                    tmp += 1

            hp[i] = [i, tmp]

    else:
        for i in range(len(minerals)//5+1):
            tmp = 0
            for j in range(i*5, i*5+5):
                if j >= len(minerals):
                    break

                tmp += 1

            hp[i] = [i, tmp]
    
    # 피로도를 기준으로 내림차순 정렬
    hp = sorted(hp, key=lambda x: x[1], reverse=True)

    for i in range(len(hp)):
        idx = hp[i][0]

        if picks[0]:
            for j in range(idx*5, idx*5+5):
                if j >= len(minerals):
                    break

                answer += 1

            picks[0] -= 1

        elif picks[1]:
            for j in range(idx*5, idx*5+5):
                if j >= len(minerals):
                    break

                if minerals[j] == 'diamond':
                    answer += 5
                else:
                    answer += 1

            picks[1] -= 1

        elif picks[2]:
            for j in range(idx*5, idx*5+5):
                if j >= len(minerals):
                    break

                if minerals[j] == 'diamond':
                    answer += 25
                elif minerals[j] == 'iron':
                    answer += 5
                else:
                    answer += 1

            picks[2] -= 1

    return answer