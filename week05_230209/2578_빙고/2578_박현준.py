def bingo_check(lst):
    bingo = 0    
    for i in lst:
        if i.count(0) == 5:
            bingo += 1
            
    for i in range(5):
        y_cnt = 0
        for j in range(5):
            if lst[j][i] == 0:
                y_cnt += 1
        if y_cnt == 5:
            bingo += 1
                
    RB_cnt = 0
    for i in range(5):
        if lst[i][i] == 0:
            RB_cnt += 1
    if RB_cnt == 5:
        bingo += 1
    
    LB_cnt = 0
    for i in range(5):
        if lst[i][4-i] == 0:
            LB_cnt += 1
    if LB_cnt == 5:
        bingo += 1
        
    return bingo

lst2 = []
lst = [[int(x) for x in input().split()] for _ in range(5)]

for i in range(5):
    lst2 += [int(x) for x in input().split()]
cnt, res = 0, 0

for k in lst2:
    for i in range(5):
        for j in range(5):
            if k == lst[i][j]:
                lst[i][j] = 0
                cnt += 1
    if cnt >= 12:
        if bingo_check(lst) >= 3:
            print(cnt)
            break