# 에너지 모으기 https://www.acmicpc.net/problem/16198
# 31256KB / 88ms
import sys
input = sys.stdin.readline

def recursion(energy):
    global ans

    # 구슬이 두개만 남으면 최대값을 계산
    if len(num) == 2:
        ans = max(ans, energy)
        return
    else:
        # 첫번째와 마지막을 제외한 구간에서 반복
        for i in range(1, len(num)-1):
            tmp = num[i-1]*num[i+1]
            now = num[i]
            num.pop(i) # 구슬을 제거했다가
            recursion(energy + tmp)
            num.insert(i, now) # 다시 리셋


n = int(input())
num = list(map(int, input().split()))
ans = 0

recursion(0)

print(ans)