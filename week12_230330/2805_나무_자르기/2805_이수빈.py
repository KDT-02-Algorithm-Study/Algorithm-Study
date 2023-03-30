# 2805 나무 자르기
# KB / ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N,M = map(int,input().split())
trees = list(map(int,input().split()))
start = 0 
end = max(trees)
ans = 0 

while start <= end :
    mid = int((start + end)/2)
    total = 0

    for t in trees:
        if t > mid :
            total += t-mid
    if total < M :                  
        end = mid -1 
    else :
        ans = mid
        start = mid + 1 

print(ans)



