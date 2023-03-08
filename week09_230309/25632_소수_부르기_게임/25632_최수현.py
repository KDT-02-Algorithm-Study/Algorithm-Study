# 메모리 31256 KB, 시간 44 ms
import sys
intput = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
m = max(b, d)

# m까지의 수를 소수 판별
is_prime = [True] * (m + 1)
for i in range(2, int(m**1/2)+1):
    if is_prime[i]:
        j = 2
        while i * j <= m:
            is_prime[i * j] = False
            j += 1

# 소수인 경우 set에 추가
prime = {i for i in range(2, m+1) if is_prime[i]}
yt = {i for i in range(a, b+1) if i in prime}
yj = {i for i in range(c, d+1) if i in prime}
# 둘의 교집합
same = yt & yj

# 교집합의 수가 홀수일 경우 각자 교집합을 뺀 수가 같을 때 용태가 이기고 짝수인 경우 유진이 이김
if len(same) & 1:
    if len(yt - same) >= len(yj - same):
        print('yt')
    else:
        print('yj')
else:
    if len(yt - same) > len(yj - same):
        print('yt')
    else:
        print('yj')