# 1157 단어 공부

data = input().upper() # 대문자로 입력
result = {} # dict 생성
for j in data:
    # if j not in result.keys():
    result[j] = result.get(j, 0) + 1
    # result[j] += 1
M = max(result.values())
count = 0
result = ''
for key, value in result.items():
    if M == value:
        count += 1
        result = key

if count > 1:   # 여러개면
    print('?')
else:
    print(result)