import sys
N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)]
dic = {}
lst_sort = sorted(lst)
for i in lst:
    dic[i] = dic.get(i, 0) + 1
dic_sort = sorted(dic.items(), key=lambda x: (x[1], -x[0]), reverse=True)
print(round(sum(lst_sort)/N))
print(lst_sort[N//2])
if len(dic_sort) > 1:
    if dic_sort[0][1] == dic_sort[1][1]:
        print(dic_sort[1][0])
    else:
        print(dic_sort[0][0])
else:
    print(dic_sort[0][0])
print(max(lst) - min(lst))