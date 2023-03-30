# 133108 KB, 788 ms
import sys
input = sys.stdin.readline

input()
sg = {}
# 카드숫자와 그 개수를 딕셔너리로 저장
for n in map(int, input().split()):
    sg[n] = sg.get(n, 0) + 1

input()
nums = list(map(int, input().split()))

for n in nums:
    print(sg.get(n, 0), end=' ')