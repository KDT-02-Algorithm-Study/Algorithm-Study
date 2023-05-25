# 한 줄로 서기 https://www.acmicpc.net/problem/1138
# 31256KB / 40ms

import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * (n+1)
order = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    # 현재 사람의 키(=i)보다 큰 사람의 수
    cnt = order[i]
    idx = 1

    # cnt가 0인 경우에도 포함하기 위하여 cnt > -1로 설정
    while cnt > -1:
        # 현재 자리(=idx)가 cnt를 만족하고, 빈 자리라면 줄 서고 반복문 탈출
        # 아니라면 다음 자리를 찾기 위해 다시 반복
        if cnt == 0:
            if ans[idx] == 0:
                ans[idx] = i
                break

        # 0인 경우는 i보다 큰 사람이 들어올 가능성이 있으니 넘어가고,
        # 이미 있는 사람의 키가 i보다 크면 넘어감
        if ans[idx] == 0 or ans[idx] > i:
            cnt -= 1
        
        idx += 1

print(' '.join(map(str, ans[1:])))