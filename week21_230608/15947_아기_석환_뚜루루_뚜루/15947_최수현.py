# 31256 KB / 44 ms
song = 'sukhwan baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby'
words = song.split()
n = int(input())
turn, seq = divmod(n, 14)

if seq in {3, 7, 11}: # tururu
    if turn > 2:
        print(f'tu+ru*{turn + 2}')
    else:
        print(words[seq] + 'ru'*turn)
elif seq in {4, 8, 12}: # turu
    if turn > 3:
        print(f'tu+ru*{turn + 1}')
    else:
        print(words[seq] + 'ru'*turn)
else: # 다른 단어들
    print(words[seq])