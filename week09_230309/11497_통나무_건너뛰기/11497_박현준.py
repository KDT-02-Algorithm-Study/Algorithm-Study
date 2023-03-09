# 34104 KB / 216 ms

T = int(input())
for _ in range(T):
    N = int(input())

    # 정렬된 리스트를 받는다
    lst = sorted([int(x) for x in input().split()])
    res = 0

    # index가 2만큼 차이나는 요소들의 차를 비교해서 최대값을 구한다
    for i in range(N-2):
        if lst[i+2] - lst[i] > res:
            res = lst[i+2] - lst[i]
    print(res)