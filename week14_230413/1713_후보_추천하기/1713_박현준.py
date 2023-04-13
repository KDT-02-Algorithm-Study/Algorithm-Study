# 31256 KB / 52 ms

N = int(input())
candidate = int(input())
# 액자
frame = []

# 투표
vote = []
lst = [int(x) for x in input().split()]

for i in range(candidate):

    # 학생이 사진에 X
    if lst[i] not in frame:

        # 사진틀에 자리가 X
        if len(frame) == N:
            for j in range(len(vote)):
                # 최소표를 찾아서 제거
                if vote[j] == min(vote):
                    del vote[j]
                    del frame[j]
                    break

        # 사진틀에 자리가 O
        frame.append(lst[i])
        vote.append(1)

    # 학생이 사진틀에 O
    else:
        for k in range(len(frame)):
            if frame[k] == lst[i]:
                vote[frame.index(frame[k])] += 1

print(' '.join(map(str, sorted(frame))))