N = int(input())
lst = [int(input()) for _ in range(N)]
dasom = lst[0]
vote = sorted(lst[1:], reverse=True)
index = 0
if N == 1:
    print(0)
else:
    while vote[0] >= dasom:
        vote[0] -= 1
        dasom += 1
        index += 1
        vote.sort(reverse=True)
    print(index)