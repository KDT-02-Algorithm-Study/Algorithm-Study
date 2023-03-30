# 150704 KB / 2152 ms

N, M = map(int, input().split())
# 정렬된 리스트를 담는다
tree = sorted([int(x) for x in input().split()])

def binary_search():
    start = 0
    # 가장 높은 길이의 나무를 end로 잡는다.
    end = tree[-1]
    while start <= end:
        mid = int((start + end) / 2)
        # 자른 나무의 값들을 담을 tmp 변수
        tmp = 0
        for i in tree:
            # 나무를 자를 수 있으면 tmp에 자른 나머지를 담는다
            if i >= mid:
                tmp += i - mid
        if tmp >= M:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
binary_search()