# 종이의 개수 https://www.acmicpc.net/problem/1780
import sys
input = sys.stdin.readline

def cut(x, y, l):
    for i in range(x, x+l):
        for j in range(y, y+l):
            if paper[i][j] != paper[x][y]:
                # 수가 같지 않으면 9개로 쪼개서 다시 탐색
                cut(x, y, l//3)
                cut(x+l//3, y, l//3)
                cut(x+l//3*2, y, l//3)
                cut(x, y+l//3, l//3)
                cut(x+l//3, y+l//3, l//3)
                cut(x+l//3*2, y+l//3, l//3)
                cut(x, y+l//3*2, l//3)
                cut(x+l//3, y+l//3*2, l//3)
                cut(x+l//3*2, y+l//3*2, l//3)
                return

    ans.append(paper[x][y])


n = int(input())
paper = [] # 입력받은 이차원 리스트
ans = [] # -1, 0, 1 개수를 입력할 리스트

for _ in range(n):
    paper.append(list(map(int, input().split())))

cut(0, 0, n)

ans = sorted(ans)

print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))