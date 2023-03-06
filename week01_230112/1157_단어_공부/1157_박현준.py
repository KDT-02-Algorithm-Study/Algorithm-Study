str = input().lower()
str_set = list(set(str))
cnt = []
for i in str_set:
    temp = str.count(i)
    cnt.append(temp)
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(str_set[(cnt.index(max(cnt)))].upper())