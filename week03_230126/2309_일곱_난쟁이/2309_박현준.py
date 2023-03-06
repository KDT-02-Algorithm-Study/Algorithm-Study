lst = []
for _ in range(9):
    lst.append(int(input()))
Sum = sum(lst)
for i in range(9):
    for j in range(i+1, 9):
        if Sum -lst[i] - lst[j] == 100:
            spy = [lst[i], lst[j]]
lst_srt = sorted(lst)
for elem in lst_srt:
    if elem not in spy:        
        print(elem)