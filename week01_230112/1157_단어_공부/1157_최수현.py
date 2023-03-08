char = {}
word = input().upper()

for i in word:
    if i in char:
        continue
    else:
        char[i] = word.count(i)

use_num = list(char.values())
most_use = max(use_num)

if use_num.count(most_use) > 1:
    print('?')
else:
    for a in char:
        if char[a] == most_use:
            print(a)
            break