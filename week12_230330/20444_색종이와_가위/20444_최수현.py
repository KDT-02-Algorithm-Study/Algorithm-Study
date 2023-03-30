# 31256 KB, 40 ms
n, k = map(int, input().split())
start = 0
# 중간지점을 끝으로 잡기
end = n//2 + 1
while start <= end:
    mid = (start + end) // 2
    # 조각의 수는 (가로 가위질 수 + 1) * (세로 가위질 수 + 1)
    paper = (mid + 1) * (n - mid + 1)

    # 같은 경우는 더 볼 것 없이 break
    if paper == k:
        print('YES')
        break
    elif paper < k:
        start = mid + 1
    else:
        end = mid - 1
        
# break 걸리지 않고 while을 다 돌면 불가능 이므로 NO
else:
    print('NO')