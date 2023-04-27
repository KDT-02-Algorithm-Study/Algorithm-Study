# 2493 탑
# 130984 KB / 632 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))
answer= [0] * n
stack = []
for i in range(len(tops)):
    # 스텍에 탑 정보가 있으면
    while stack:
        # 지금 탐색하는 탑의 높이가 스택의 top보다 크다면
        if tops[stack[-1][0]]<tops[i]:
            stack.pop()
        # 작다면
        else:
            # 탑의 위치를 저장
            answer[i] = stack[-1][0]+1
            break
    # 삽입
    stack.append((i,tops[i]))
print(*answer)