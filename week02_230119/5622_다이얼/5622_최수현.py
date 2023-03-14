dial = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7,
        'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
word = list(input())
time = 0

for a in dial:
    for w in word:
        if w in a:
            time += dial[a]

print(time)