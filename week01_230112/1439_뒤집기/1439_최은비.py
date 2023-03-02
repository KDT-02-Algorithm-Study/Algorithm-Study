# 코드 작성 아이디어
# 1. 1을 0으로 뒤집는 횟수 카운팅 변수 count_0, 0을 1로 뒤집는 횟수 카운팅 변수 count_1 만들기
# 2. 뒤집는 타이밍은 연속이 끝났을 때, 즉 현재 문자와 다음 문자가 다를 때
# 3. 다만 마지막 문자는 비교할 다음 문자가 없으므로 비교하는 범위는 문자열 길이보다 1 적어야 함
# 4. 첫글자에 대해 카운팅을 처리하지 않으면 횟수가 하나 부족해지므로 첫글자도 처리해줘야 함


# 1439 

s = input()

count_1 = 0
count_0 = 0

if s[0] == '0':
    count_1 += 1
else:
    count_0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count_0 += 1
        else:
            count_1 += 1

print(count_0, count_1)
print(min(count_0, count_1))