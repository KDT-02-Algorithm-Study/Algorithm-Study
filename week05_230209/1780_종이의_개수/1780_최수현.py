import sys

def unify(paper):
    if len(paper[0]) == 1:
        cnt[paper[0][0]+1] += 1
        return
    else:
        boolean = False
        for i in range(len(paper[0])):
            for j in range(len(paper[0])):
                if paper[i][j] != paper[0][0]:
                    boolean = False
                    break
            else:
                boolean = True
            if not boolean:
                break
        if boolean:
            cnt[paper[0][0]+1] += 1
            return
        else:
            l = len(paper[0])//3
            for i in range(0, len(paper[0]), l):
                for j in range(0, len(paper[0]), l):
                    div = []
                    for y in range(i, i+l):
                        div.append(paper[y][j:j+l])
                    unify(div)

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = [0, 0, 0]
unify(paper)
print(*cnt, sep='\n')