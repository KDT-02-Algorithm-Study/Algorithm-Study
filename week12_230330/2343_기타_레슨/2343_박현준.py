# 42340 KB / 228 ms

def binary_search(value):
    start = max(lst)
    end = sum(lst)
    while start <= end:
        mid = int((start + end) / 2)
        cnt = 1
        tmp = 0
        for i in range(N):
            tmp += lst[i]
            if tmp > mid:
                cnt += 1
                tmp = lst[i]

        if cnt > value:
            start = mid + 1
        else:
            end = mid - 1
    print(end+1)

N, M = map(int, input().split())
lst = [int(x) for x in input().split()]
binary_search(M)