# 1713 후보 추천하기
# 31256 KB / 44 ms

n = int(input()) # 사진틀 개수
r = int(input()) # 추천 횟수
s = list(map(int, input().split())) # 추천 순서

# dict에 담으면서 추천 순서대로 탐색
result = {}
for i in range(r):
    if s[i] in result: # 이미 있을 때
        result[s[i]][0] += 1 
    else:
        if len(result) < n:
            result[s[i]] = [1, i] # { s[i]: [1, i] } # [추천 횟수, 들어온 순서]
        else: # 가득 찼을 때
            temp = sorted(result.items(), key=lambda x: (x[1], x[0])) # 다중조건 정렬 
            result.pop(temp[0][0]) # pop하고
            result[s[i]] = [1, i] # 추가

# 정렬 후 출력
print(' '.join(map(str, sorted(result.keys()))))