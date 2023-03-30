# 15810 풍선 공장
# 150704 KB / 4672 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N,M = map(int,input().split())
effort = list(map(int,input().split()))

start = (M // N) * min(effort)
end = (M // N +1) * max(effort) 
ans = 0

while start <= end :
    total = 0
    mid = int((start+end)/2)
    for e in effort: # mid의 시간을 주었을 때 몇 개의 풍선을 만들 수 있는가? 
        total += int(mid/e)
    if total >= M :
        ans = mid
        end = mid-1
    else :
        start = mid + 1
print(ans)