# 후보 추천하기 https://www.acmicpc.net/problem/1713
# 31256KB / 44ms
import sys
input = sys.stdin.readline

def min_candidate():
    lst = []
    min_cnt = min(cnt.values())

    for i in cnt:
        if cnt[i] == min_cnt:
            lst.append(i)

    return lst


n = int(input())
num = int(input())
stu = list(map(int, input().split()))
# 후보자 명단
candidate = []
# 후보자 추천수
cnt = {}

for i in range(num):
    # 학생이 후보자 명단에 없을 때
    if stu[i] not in candidate:
        # 비어있는 사진틀이 있는 경우
        if len(candidate) < n:
            candidate.append(stu[i])
            cnt[stu[i]] = 1
        else:
            # 추천 횟수가 가장 적은 학생
            idx = min_candidate()[0]
            del cnt[idx]
            candidate.remove(idx)
            candidate.append(stu[i])
            cnt[stu[i]] = 1

    else:
        cnt[stu[i]] += 1

candidate = sorted(candidate)
print(*candidate)