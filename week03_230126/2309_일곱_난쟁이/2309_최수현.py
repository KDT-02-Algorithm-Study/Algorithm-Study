dwarf = []
for i in range(9):
    dwarf.append(int(input()))

not_dwarf = sum(dwarf) - 100
k = 0
while len(dwarf) == 9:
    for j in range(9):
        if j == k:
            continue
        if dwarf[j] + dwarf[k] == not_dwarf:
            dwarf.pop(j)
            dwarf.pop(k)
            break
    k += 1
        
print(*sorted(dwarf), sep='\n')