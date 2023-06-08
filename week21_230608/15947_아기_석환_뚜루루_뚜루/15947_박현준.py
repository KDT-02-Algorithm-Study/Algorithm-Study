song = ['baby','sukhwan','tururu','turu','very','cute','tururu','turu','in','bed','tururu','turu','baby','sukhwan',]

N = int(input())
repeat = N // 14
index = N % 14 - 1
if 'turu' not in song[index]:
    print(song[index])
else:
    S = song[index]
    res = S + 'ru' * repeat
    ru_count = res.count('ru')
    if ru_count >= 5:
        print(f'tu+ru*{ru_count}')
    else:
        print(res)