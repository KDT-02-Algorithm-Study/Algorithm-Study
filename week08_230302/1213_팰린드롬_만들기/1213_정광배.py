# 1213 팰린드롬 만들기
# 34104 KB / 64 ms

from collections import Counter

data = Counter(input()) # Counter로 문자열 입력받아서 저장
flag = 0 # 홀수의 개수를 저장할 변수
c = '' # 가운데 문자를 저장할 변수

for k, v in data.items():
    if v%2 == 1: # 문자가 홀수개인지 판별
        if not flag: # 첫 번째 홀수이면
            c = k   # 그 문자를 c에 저장
            flag=1
        else: # 두 번째 홀수이면 출력 후 종료
            print("I'm Sorry Hansoo")
            exit()
    data[k]=v//2 # 개수의 반만 저장

data = dict(sorted(data.items())) # 사전순 정렬 후 dict 으로 저장

result = ''
for k, v in data.items():
    result += k*v
print(result+c+result[::-1]) # 앞부분 + c + 뒷부분