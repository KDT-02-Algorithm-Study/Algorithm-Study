# 13458 시험 감독

# 시험장의 개수
N = int(input())
# 시험장의 응시자 수
A = list(map(int, input().split()))
# 총감독관, 부감독관 감시수
B, C = map(int, input().split())

cnt = 0
for a in A:
    a -=B # 총감독관
    cnt += 1
    if a > 0:
        # 부감독관
        if a % C == 0:
            cnt += a//C
        else:
            cnt += a // C + 1
        # cnt += -(-a//C)
print(cnt)