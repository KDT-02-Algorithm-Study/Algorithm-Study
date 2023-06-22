# 광물 캐기
# 테스트 13 〉	통과 (0.04ms, 10.2MB)

import heapq

def get_stamina(pick, mineral):
    if pick == 0:
        stamina = sum(mineral)
    elif pick == 1:
        stamina = mineral[0]*5 + mineral[1] + mineral[2]
    else:
        stamina = mineral[0]*25 + mineral[1]*5 + mineral[2]
    return -stamina     # 


def solution(picks, minerals):
    answer = 0
    g = sum(picks)                  # 곡괭이 총 개수
    t = min(len(minerals), g*5)     # 곡괭이*5와 광물 개수 중에 적은것을 채택
    r = []

    # 5개씩 끊어서 광물을 변환 후 '최대힙'으로 저장
    # 광물 개수가 5개 보다 적어도 25 5 1 로 계산되기 때문에 'diamond'가 더 많을 때 'diamond 곡괭이'로 캐는 것이 이득
    for i in range(0, t, 5):
        now = minerals[i:i+5]
        a = [0]*3
        for j in now:
            if j == 'diamond':
                a[0] -= 1
            elif j == 'iron':
                a[1] -= 1
            else:
                a[2] -= 1
        heapq.heappush(r, a)

    # 최대힙을 pop하면서 피로도 계산
    while r:
        b = heapq.heappop(r)
        if picks[0]:
            answer += get_stamina(0, b)
            picks[0] -= 1
        elif picks[1]:
            answer += get_stamina(1, b)
            picks[1] -= 1
        elif picks[2]:
            answer += get_stamina(2, b)
            picks[2] -= 1

    return answer



# 시간초과
# 모든 곡괭이 순서를 뽑아서 최솟값 완전 탐색

# import itertools

# def solution(picks, minerals):
#     answer = 1000000
#     p = []
#     for j in range(3):
#         p.extend([j]*picks[j])
#     per = set(itertools.permutations(p, len(p)))
#     for su in per:
#         r = 0
#         s = 0
#         su = list(su)
#         for i in range(0, len(minerals), 5):
#             now = minerals[i:i+5]
#             method = su[s]
#             for j in now:
#                 if j == 'diamond':
#                     if method == 0:
#                         r += 1
#                     elif method == 1:
#                         r += 5
#                     else:
#                         r += 25
#                 elif j == 'iron':
#                     if method == 0:
#                         r += 1
#                     elif method == 1:
#                         r += 1
#                     else:
#                         r += 5
#                 else:
#                     r += 1
#             s += 1
#             if s >= len(su):
#                 break
#         if r < answer:
#             answer = r
#     return answer