# 색종이와 가위 https://www.acmicpc.net/problem/20444
# 31256KB / 44ms
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 총 가위질 횟수
s = 0
e = n

while s <= e:
    mid = int((s+e) / 2) # 가로 가위질
    tmp = n - mid # 세로 가위질

    # 잘라서 만든 조각이 목표 조각보다 크면 가위질 횟수를 늘림(왜지..)
    if (mid+1) * (tmp+1) > k:
        s = mid + 1
    elif (mid+1) * (tmp+1) < k:
        e = mid - 1
    else:
        print("YES")
        break
else:
    print("NO")