# 2503 숫자 야구 https://www.acmicpc.net/problem/2503
# 31256KB / 100ms

import sys
input = sys.stdin.readline

n = int(input())
ques = []
ans = []
cnt = 0
# 서로 다른 숫자 세개로 만들 수 있는 가장 작은 수로 초기화
mh = '123'

for _ in range(n):
    a, b, c = map(int, input().split())
    ques.append(str(a))
    ans.append((b, c))

# 123부터 1씩 더해가면서 조건 확인
while int(mh) != 999:
    # 겹치는 숫자가 있거나 0이 포함되면 조건을 확인할 필요 X
    if len(set(mh)) == 3 and '0' not in mh:
    
        tmp = 0

        # 질문 개수만큼 반복
        for i in range(n):
            s = b = 0
            # 숫자가 세개니까 3번 반복
            for j in range(3):
                # 같은 자리에 있으면 스트라이크에 +1
                if ques[i][j] == mh[j]:
                    s += 1
                # 다른 자리에 있으면 볼에 +1
                elif mh[j] in ques[i] :
                    b += 1    
            # 영수가 대답한 스트라이크, 볼 수와 위에서 체크한 스트라이크, 볼 수가 같으면
            if s == ans[i][0] and b == ans[i][1]:
                tmp += 1
        # tmp가 n이랑 같다는 말은 질문을 다 만족한다는 말이니까 정답일 가능성이 있음
        # 질문 n개 중에 하나라도 만족하지 않으면 cnt에 포함하면 안됨
        if tmp == n:
            cnt += 1

    mh = str(int(mh) + 1)
    
print(cnt)