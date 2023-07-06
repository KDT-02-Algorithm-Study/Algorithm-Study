# 정확성: 75 / 75
# 효율성: 10 / 25
# 합계: 85.0 / 100.0

def solution(people, limit):
    people.sort()
    check = [False] * len(people)
    i = 0
    ans = 0
    
    while 1:
        # 방문한 경우 건너뛰기
        if check[i]:
            i += 1
            continue
        
        # 방문하지 않은 경우
        # 어차피 태워야하므로 방문처리 & ans +1하고 시작
        check[i] = True
        ans += 1

        # 같이 탈 수 있는 사람 중 무게가 가장 많이 나가는 사람 고르기
        max_pair = 0
        for j in range(i+1,len(people)):
            if not check[j] and people[i] + people[j] <= limit:
                max_pair = j
            else:
                break
        
        # 같이 탈 수 없는 사람이 없으면 뒤에도 어차피 없으므로 break
        if max_pair == 0:
            break
        else:
            check[max_pair] = True
            i += 1
    
    # 보트에 못 탄 사람 보트 하나씩 써야함
    ans += len(check) - sum(check)
    
    return ans