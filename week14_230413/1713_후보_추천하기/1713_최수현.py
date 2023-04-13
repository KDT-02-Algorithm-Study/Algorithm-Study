# 31256 KB / 40 ms
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
rec = list(map(int, input().split()))
vote = {}   # 사진이 걸린 학생의 번호: 투표수
seq = []    # 사진이 걸린 순서

for i in range(m):
    # 사진이 걸린 학생이면 그냥 +1
    if rec[i] in vote:
        vote[rec[i]] += 1

    # 사진이 안걸린 학생인 경우
    else:
        # 사진틀이 다 찼으면 투표수가 가장 적은 학생 제거
        if len(vote) == n:
            min_vote = min(vote.values())
            for j in range(len(seq)):
                if vote[seq[j]] == min_vote:
                    vote.pop(seq[j])
                    seq.pop(j)
                    break
        # 제거 후 새로운 학생 게시
        vote[rec[i]] = 1
        seq.append(rec[i])

print(*sorted(vote.keys()))