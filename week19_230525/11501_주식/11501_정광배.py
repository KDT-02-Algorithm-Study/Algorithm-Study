# 11501 주식
# 169620 KB / 6472 ms

from collections import Counter

T = int(input())
for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    data_c = Counter(data)

    total = 0
    m = max(data_c)
    for i in data: # data 순회
        if i != m: # 최댓값이 아니면 구매
            total += m-i # 최댓값 - 구매가

        # 확인한 숫자 감소시키기
        if data_c[i] == 1: 
            data_c.pop(i)
            if i == m and data_c:
                m = max(data_c) # 최댓값 갱신
        else:
            data_c[i] -= 1
    print(total)