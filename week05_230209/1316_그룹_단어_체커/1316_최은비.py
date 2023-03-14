# https://www.acmicpc.net/problem/1316
# 접근법
# 1. 단어를 입력받고 빈 리스트와 그룹단어인지 체크할 변수를 선언한다
# 2. 단어를 순회하면서 알파벳이 리스트에 없으면 넣고, 있다면 이전 알파벳과 비교해서 같은 알파벳이면 무시,
#    다른 알파벳이면 그룹 단어가 아니므로 반복문을 빠져나간다.
# 3. 입력받은 단어 개수만큼 반복하면서 그룹단어가 몇개인지 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for i in range(n):
    word = input().strip()
    check = []
    is_group = True

    for j in range(len(word)):
        if word[j] not in check:
            check.append(word[j])
        else:
            if word[j] == word[j-1]:
                continue
            else:
                is_group = False
                break

    if is_group:
        cnt += 1

print(cnt)
        