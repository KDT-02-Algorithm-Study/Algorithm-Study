# 11478 서로 다른 부분 문자열의 개수
# 240916 KB / 512 ms

data = input()
result = set()
# 모든 경우의 수를 set에 add 
for i in range(len(data)):
    for j in range(i+1, len(data)+1):
        result.add(data[i:j])
print(len(result))