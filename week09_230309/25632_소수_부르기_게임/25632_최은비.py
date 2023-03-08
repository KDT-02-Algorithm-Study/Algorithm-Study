# 25632 소수 부르기 게임 https://www.acmicpc.net/problem/25632
# 31256KB / 40ms

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
prime = [1] * 1001

# 인덱스가 소수면 1, 아니면 0인 리스트 만들기
for i in range(2, int((1000)**0.5)+1):
    if prime[i] == 1:
        for j in range(i+i, 1001, i):
            prime[j] = 0

# 용태와 유진이가 부를 수 있는 소수가 겹치면 그 개수를 구하고
if b >= c:
    tmp = sum(prime[c:b+1])
else:
    tmp = 0

# 각자가 부를 수 있는 소수 전체 개수에서 겹치는 개수를 빼줌
yt = sum(prime[a:b+1]) - tmp
yj = sum(prime[c:d+1]) - tmp

# 겹치는 소수가 짝수개일 때와 홀수개일 때 결과가 달라지므로 나눠서 누가 이기는지를 출력
if tmp % 2 == 0:
    if yt > yj:
        print("yt")
    else:
        print("yj")
else:
    if yt >= yj:
        print("yt")
    else:
        print("yj")