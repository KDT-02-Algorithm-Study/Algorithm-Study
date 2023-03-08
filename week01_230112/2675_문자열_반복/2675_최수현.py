t = int(input())

for i in range(t):
    r, word = input().split()
    new_word = []

    for a in word:
        new_word.append(a*int(r))
    
    print(''.join(new_word))