bowl = input()
l = 10
for i in range(len(bowl)-1):
    if bowl[i] == bowl[i+1]:
        l += 5
    else:
        l += 10
print(l)