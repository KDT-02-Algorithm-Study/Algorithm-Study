# 메모리 31256 KB, 시간 316 ms
import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
length = sorted([int(input()) for _ in range(n)])
# 가장 큰 길이 x 가격을 넣고 시작
max_money = length[-1] * w

if n == 1:
    print(max_money)
else:
    # 1부터 두번째로 큰 수까지만 보면 됨
    for x in range(1, length[-2]+1):
        money = 0
        for l in length:
            d, m = divmod(l, x)
            # 나누어떨어지면 몫-1, 그렇지 않으면 몫만큼 c를 냄
            if m == 0:
                # 값이 0보다 클 경우만 더해줌
                if x*d*w - c*(d-1) > 0:
                    money += x*d*w - c*(d-1)
            else:
                if x*d*w - c*d > 0:
                    money += x*d*w - c*d

        if money > max_money:
            max_money = money

    print(max_money)