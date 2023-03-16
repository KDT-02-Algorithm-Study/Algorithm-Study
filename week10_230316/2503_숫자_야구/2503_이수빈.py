# 2503 숫자 야구
# KB / ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
ques = []
for i in range(n):
    ques.append(list(map(int,input().split())))

print(ques)
