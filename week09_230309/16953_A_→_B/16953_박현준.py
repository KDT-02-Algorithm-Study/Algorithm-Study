# 31256 KB / 40 ms

A, B = map(int, input().split())
cnt = 0
while True:

    # 연산 횟수 증가
    cnt += 1

    # 종료 조건
    if A == B:
        print(cnt)
        break

    # B를 담을 임시 변수 tmp
    tmp = B

    # B의 가장 오른쪽에 1이 있으면
    if B % 10 == 1:

        # 1을 제거한다.
        B //= 10
    
    # B를 2로 나눌 수 있으면
    elif B % 2 == 0:

        # B를 2로 나눈다
        B //= 2
    
    # 만약 연산 후에도 B랑 같으면 무한 루프를 돌기 때문에 탈출한다.
    if tmp == B:
        print(-1)
        break