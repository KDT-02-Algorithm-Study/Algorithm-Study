T = int(input())
for _ in range(T):
    floor = int(input())
    num = int(input())
    lst = [x for x in range(1, num+1)]
    for _ in range(floor):
        for i in range(1, num):
            lst[i] += lst[i-1]
    print(lst[-1])