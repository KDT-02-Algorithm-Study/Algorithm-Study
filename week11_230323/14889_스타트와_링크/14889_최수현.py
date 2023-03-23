# 37960 KB, 2504 ms
import sys
input = sys.stdin.readline

def team_maker(check, s):
    # 한 팀이 완성된 경우
    if sum(check) == n//2:
        team_a = [i for i in range(n) if check[i]]
        team_b = [i for i in range(n) if not check[i]]
        a = b = 0

        # 각 팀의 능력치 계산
        for i in team_a:
            for j in team_a:
                a += stat[i][j]
        for i in team_b:
            for j in team_b:
                b += stat[i][j]

        result.append(abs(a - b))
        return

    # 이전에 추가했던 값 이후의 인덱스부터 시작
    for i in range(s, n):
        if not check[i]:
            check[i] = True
            team_maker(check, i+1)
            check[i] = False

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
is_used = [False] * n
result = []
team_maker(is_used, 0)  # 0은 현재 인덱스 표시
print(min(result))