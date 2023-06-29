# 두 큐 합 같게 만들기
# 테스트 24 〉	통과 (77.60ms, 37.9MB)

from collections import deque

def solution(q1:list, q2:list):
    l = len(q1)
    s1 = sum(q1)
    s2 = sum(q2)

    # 합이 홀수일 경우 -1 반환
    if (s1 + s2) % 2:
        return -1

    q1=deque(q1)
    q2=deque(q2)
    cnt = 0
    while cnt <= l*3:
        # 같으면 탈출
        if s1 == s2:
            return cnt

        # s1과 s2 비교
        if s1 > s2:
            t = q1.popleft()
            q2.append(t)
            s1 -= t
            s2 += t
        elif s1 < s2:
            t = q2.popleft()
            q1.append(t)
            s1 += t
            s2 -= t
        cnt += 1
    return -1 # 탈출 못했을 경우 -1 반환
    