# 2502 떡 먹는 호랑이
# 31256 KB / 44 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

d, k = map(int, input().split())

x = 1
y = 0
# 피보나치 구하기 
for i in range(d-1):
    x, y = y, x+y 
    # y -> d번째 피보나치 수/ x -> d-1번째 피보나치 수
for a in range(1, 100000): 
    if (k-(x*a))%y == 0: # 나누어 떨어진다면, 몫이 b가 됨.
        print(a, (k-(x*a))//y, sep="\n")
        break
