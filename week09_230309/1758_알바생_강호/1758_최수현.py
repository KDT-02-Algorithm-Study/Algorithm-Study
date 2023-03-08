# 메모리 35892 KB, 시간 3804 ms
import sys
intput = sys.stdin.readline

n = int(input())
# 역순 정렬
tips = sorted([int(input()) for _ in range(n)], reverse=True)
total = 0

for i in range(n):
    # 받을 수 있는 팁이 0이하가 되는 시점에서 종료
    if tips[i] - i <= 0:
        break
    total += tips[i] - i

print(total)