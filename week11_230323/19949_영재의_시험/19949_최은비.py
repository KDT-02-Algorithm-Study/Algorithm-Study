# 영재의 시험 https://www.acmicpc.net/problem/19949
# 31388KB / 344ms
import sys
input = sys.stdin.readline

def exam(cnt, correct):
    global ans

    if cnt == 10:
        ans += 1
        return
    
    for i in range(1, 6):
        # 문제가 두개 이하일 땐 아무 번호나 넣어도 됨
        # 두개 이상이 되면 직전 두개랑 다른 번호만 넣어야 됨
        if len(yj) < 2 or (yj[-1] != i or yj[-2] != yj[-1]):
            yj.append(i)
            # 방금 넣은 번호가 정답이면 맞은 개수에 +1 하고
            if num[len(yj)-1] == i:
                exam(cnt+1, correct+1)
            else:
                # 남은 문제가 전부 정답이어도 5점을 넘지 않으면 영재 답에서 하나 빼고 다음 재귀를 돌지 않음
                if len(yj) - correct > 5:
                    yj.pop()
                    continue
                
                exam(cnt+1, correct)
            yj.pop()


num = list(map(int, input().split()))
yj = []
ans = 0
# 문제 개수, 정답 개수
exam(0, 0)

print(ans)