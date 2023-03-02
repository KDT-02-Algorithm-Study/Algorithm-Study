# 팰린드롬 만들기 https://www.acmicpc.net/problem/2477
# 31388KB, 44ms
# 알파벳 횟수로 팰린드롬을 만들 수 있는지 확인
# - 이름 길이가 짝수일 때, 이름에 있는 모든 알파벳은 짝수개여야 함
# - 이름 길이가 홀수일 때, 이름에 있는 알파벳 중 하나는 홀수여도 됨

import sys
input = sys.stdin.readline

name = sorted(list(input().strip())) # 사전순으로 출력해야하므로 정렬해서 입력 받기
alpha_dict = {} # 이름에 등장하는 알파벳 횟수를 저장할 딕셔너리
res = ""
odd = "" # 이름 길이가 홀수일 경우, 홀수개인 알파벳을 저장할 변수

for i in name:
    if i in alpha_dict:
        alpha_dict[i] += 1
    else:
        alpha_dict[i] = 1

for char, num in alpha_dict.items():
    # 알파벳 개수가 1개 이상이라면 결과 변수에 붙여주기
    while num > 1:
        res += char
        num -= 2 # 앞뒤로 두번 사용되므로 -2
        
    if num == 1:
        # 알파벳이 하나 남았는데 이름 길이가 짝수면 팰린드롬으로 만들 수 없으므로 반복문 종료
        if len(name) % 2 == 0:
            print("I'm Sorry Hansoo")
            break
        else:
            # 이름 길이가 홀수인데 홀수개인 알파벳이 하나도 없었으면 따로 저장
            if not odd:
                odd = char
            else:
                # 이미 홀수개인 알파벳이 있었다면 팰린드롬을 만둘 수 없으므로 반복문 종료
                print("I'm Sorry Hansoo")
                break
else:
    if len(name) == 0: # 저장한 결과 변수를 한 번 출력하고 뒤집어서 한 번 더 출력
        print(res, res[::-1], sep="")
    else: # 이름 길이가 홀수면 중간에 홀수개인 알파벳을 함께 출력
        print(res, odd, res[::-1], sep="")