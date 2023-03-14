# 14247 나무 자르기
# 42572 KB / 116 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
tree = list(map(int,input().split()))
grow = list(map(int,input().split()))

TRnGR = list(zip(tree,grow))
S_TRnGR = sorted(TRnGR, key = lambda x : x[1])

res = 0 
for i in range(n):
    res += S_TRnGR[i][0] + (S_TRnGR[i][1]*i)

print(res)

