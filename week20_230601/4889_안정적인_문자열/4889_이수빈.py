# 4889 안정적인 문자열
# 31256 KB / 48 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

cnt = 0 
while True :
    res = 0 
    str_list = input()
    bracket = []
    if str_list[0] == '-':
        break

    for b in str_list:
        if not bracket and b == '}':
            res += 1
            bracket.append('{') # 바꿔주어야하니까
        elif bracket and b == '}':
            bracket.pop()
        else:
            bracket.append(b)
    cnt += 1 
    res += int(len(bracket)/2)
    print(f'{cnt}. {res}')
