# 31596 KB, 96 ms
import sys
input = sys.stdin.readline

# m은 현재 변화된 근육량
def get_muscle(check, m):
    # 키트 n개를 다 쓰면 cases에 1 추가 후 리턴
    if sum(check) == n:
        cases.append(1)
        return

    for i in range(n):
        # 현재 근육량 + 득근량 - 근손실량이 0이상인지 확인
        if not check[i] and m + growth[i] - k >= 0:
            check[i] = True
            get_muscle(check, m + growth[i] - k)
            check[i] = False

n, k = map(int, input().split())
growth = list(map(int, input().split()))
# check list 생성
is_used = [False] * n
cases = []
get_muscle(is_used, 0)
print(sum(cases))