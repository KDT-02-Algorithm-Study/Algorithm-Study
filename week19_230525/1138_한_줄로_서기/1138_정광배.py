# 1138 한 줄로 서기
# 31256 KB / 44 ms


n = int(input())
data = list(map(int, input().split())) # 2 1 1 0
result = [0]*n
visited = [False]*n
for i, v in enumerate(data, 1):
    cnt = 0 # 빈자리 카운트
    for j in range(n): # result index
        if cnt == v and not visited[j]: # 빈자리와 v가 같을 때
            result[j] = i # result에 저장
            visited[j] = True # 방문 처리
            break # 
        if result[j] == 0:
            cnt += 1 # 빈자리
print(' '.join(map(str, result)))


'''
0 0 1 0
0 2 1 0
0 2 1 3
4 2 1 3
'''

'''
7
6 1 1 1 2 0 0

6 2 3 4 7 5 1
'''


# 맞왜틀?? # 반례?
""" n = int(input())
data = list(map(int, input().split())) # 2 1 1 0
line = [i for i in range(n)] # 0 1 2 3
visited = [False]*n
result = [0]*n
for i, v in enumerate(data, 1):
    for ii, vv in enumerate(line):
        if v == vv and not visited[ii]:
            result[ii] = i # result에 저장
            visited[ii] = 1 # 방문처리
            for j in range(v+1, n): # 뒷자리 -1씩
                if line[j]:
                    line[j] -= 1
            break
print(' '.join(map(str, result))) """