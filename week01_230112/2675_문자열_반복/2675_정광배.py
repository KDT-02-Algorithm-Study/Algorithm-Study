# 2675 문자열 반복

T = int(input())

for _ in range(T):
    result = ''
    r, s = input().split()

    for i in s:
        for _ in range(int(r)):
            result += i
    print(result)