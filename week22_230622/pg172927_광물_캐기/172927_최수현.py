def solution(picks, minerals):
    answer = 0
    level = []  # 5개씩 나눈 각 구간의 난이도 측정하여 담을 리스트

    # 난이도 측정
    # 범위 : 도끼로 캘 수 있는 광물 수와 주어진 광물 수 중 작은값까지 -> 작업이 끝나는 시점
    for i in range(0, min(sum(picks)*5, len(minerals)), 5):
        cnt = 0  # 난이도 count
        for j in range(5):
            # index 벗어나면 break
            if i + j >= len(minerals):
                break
            # 돌도끼 기준으로 난이도 측정
            x = minerals[i+j]
            if x == 'diamond':
                cnt += 25
            elif x == 'iron':
                cnt += 5
            else:
                cnt += 1
        # 난이도와 5개 광물의 시작 인덱스 함께 append
        level.append((cnt, i))
    level.sort(key=lambda x: x[0], reverse=True) # 난이도 높은 순서로 정렬

    for cnt, i in level:
        # 도구를 쎈 순서로 선택
        for j in range(3):
            if picks[j] > 0:
                picks[j] -= 1
                tool = j
                break
        
        # 피로도 측정
        for k in range(5):
            # index 벗어나면 break
            if i + k >= len(minerals):
                break

            # 광물의 값을 도구 index와 맞추기
            if minerals[i+k] == 'diamond':
                mineral = 0
            elif minerals[i+k] == 'iron':
                mineral = 1
            else:
                mineral = 2

            if tool > mineral:
                answer += 5 ** (tool-mineral)
            else:
                answer += 1

    return answer
