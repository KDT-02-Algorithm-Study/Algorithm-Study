# 코드 작성 아이디어
# 1. 테스트 개수 만큼 반복하는 for문 하나
# 2. 반복 횟수만큼 문자를 반복하는 for문 하나
# 3. 문자를 출력하기 위한 for문 하나

# 2675 

import sys

test = int(sys.stdin.readline().split())

for i in range(test):
    string = sys.stdin.readline().split()
    for j in range(2, len(string)):
        for k in range(int(string[0])):
            print(string[j], end='')
    print()