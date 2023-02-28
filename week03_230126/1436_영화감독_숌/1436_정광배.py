# 1436 영화감독 숌

n = int(input())

cnt = 0
i = 0
while cnt < n:
    i += 1
    if '666' in str(i): # 전수조사
        cnt += 1
    
print(i)