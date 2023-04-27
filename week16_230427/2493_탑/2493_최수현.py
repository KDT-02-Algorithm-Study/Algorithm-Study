# 86700 KB / 600ms
import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []

for i in range(n):
    # 이번에 넣어야 할 값보다 작은 값은 모두 pop
    while stack and towers[stack[-1]] <= towers[i]:
        stack.pop()

    if stack:
        print(stack[-1] + 1, end=' ')
    else:
        print(0, end=' ')

    stack.append(i)