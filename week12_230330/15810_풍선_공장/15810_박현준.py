# 150704 KB / 3328 ms

def binary_search(lst):
    start = 0
    # 가장 오래걸리는 스태프가 모든 풍선을 부는 값을 end로 설정
    end = max(lst) * M
    while start <= end:
        # 풍선을 담을 total 변수
        total = 0
        mid = int((start + end) / 2)
        # mid 시간동안 스태프들이 불 수 있는 풍선의 합
        for i in A:
            total += int(mid / i)        
        if total < M:
            start = mid + 1
        else:
            end = mid - 1
    print(end + 1)


N, M = map(int, input().split())
A = [int(x) for x in input().split()]

binary_search(A)