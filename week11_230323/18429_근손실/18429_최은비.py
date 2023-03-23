# 근손실 https://www.acmicpc.net/problem/18429
# 31256KB / 124ms
import sys
input = sys.stdin.readline

def recursion(cnt):
    global ans 
    # 입력으로 주어진 일수만큼 반복하면 중량 계산
    if cnt == n:
        total = 500

        for i in tmp:
            total += weight[i] - k
            # 중량이 500으로 떨어지만 카운트를 하지 않고 돌아가기
            if total < 500:
                break

        if total >= 500:
            ans += 1
        
        return
    
    for i in range(n):
        if i not in tmp:
            tmp.append(i)
            recursion(cnt+1)
            tmp.pop()


n, k = map(int, input().split())
weight = list(map(int, input().split()))
tmp = []
ans = 0

recursion(0)

print(ans)