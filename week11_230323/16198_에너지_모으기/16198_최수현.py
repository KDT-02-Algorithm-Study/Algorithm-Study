# 32620 KB, 116 ms
import sys
input = sys.stdin.readline

def energe(check, total):
    # 가능한 모든 구슬 제거 시 리스트에 총합 추가 후 리턴
    if sum(check) == n-2:
        result.append(total)
        return
    
    # 양 끝을 제외한 범위
    for i in range(1, n-1):
        if not check[i]:
            # 방문처리 == 구슬 제거
            check[i] = True

            # 제거되지 않은 구슬이 나올 때까지 a, b +-1
            a = b = i
            while check[a]:
                a -= 1
            while check[b]:
                b += 1
            energe(check, total + balls[a] * balls[b])
            check[i] = False

n = int(input())
balls = list(map(int, input().split()))
is_used = [False] * n
result = []

energe(is_used, 0)  # 방문 리스트와 현재 에너지 합계
print(max(result))