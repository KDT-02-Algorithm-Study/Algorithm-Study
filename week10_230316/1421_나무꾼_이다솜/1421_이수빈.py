# 1421 나무꾼 이다솜
# 33376KB / 284ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from math import ceil 

n, c, w = map(int, input().split())
trees = []
for _ in range(n):
   trees.append(int(input()))
profits=[]

# 1부터 제일 긴 나무의 길이만큼 자름 
for L in range(1,max(trees)+1):
  profit = []
  # 
  for tree in trees:
      # 나무별로 잘라서 파는 금액보다 자르는데 드는 비용이 더 크다면.. 안파는게 나을 수도 있음 
      # 0이랑 비교해서, 음수면 걍 0이 저장되도록 함
      profit.append(max(0,(tree // L)*L*w - (ceil(tree / L)-1)*c)) # 파는 비용 - 자르는 비용
  profits.append(sum(profit))
print(max(profits))