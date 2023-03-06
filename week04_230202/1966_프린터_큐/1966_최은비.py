# https://www.acmicpc.net/problem/1966

import sys
from collections import deque

test = int(input())

for _ in range(test):
    num, idx = map(int, input().split())
    numbers = list(map(int, input().split()))
    que = deque()
    cnt = 0

    for n in numbers:
        que.append(n)

    while True:
        max_ = max(que)
        # que의 맨 앞 요소 확인
        tmp = que.popleft()
        idx -= 1

        # tmp가 최대값이고
        if tmp == max_:
            cnt += 1
            # idx가 0보다 작으면 입력으로 주어진 문서이므로 출력
            # (if문 들어오기 전에 -1을 해줘서 맨 앞에 요소 인덱스는 0보다 작아짐)
            if idx < 0:
                print(cnt)
                break
        # tmp가 최대값이 아니면 맨 뒤에 삽입
        else:
            que.append(tmp)
            # idx가 0보다 작아지면 que 맨 마지막 인덱스로 바꿔주기
            if idx < 0:
                idx = len(que) -1