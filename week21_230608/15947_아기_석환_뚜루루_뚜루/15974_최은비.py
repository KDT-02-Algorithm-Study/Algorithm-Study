# 아기 석환 뚜루루 뚜루 https://www.acmicpc.net/problem/15947
# 31256KB / 40ms
import sys
input = sys.stdin.readline

song = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']
n = int(input())
repeat = n // 14
ans = song[n % 14 - 1]

if ans[0] == 't':
    if repeat > 2 and n % 14 in [3, 7, 11]:
        print(f'tu+ru*{repeat+2}')
    elif repeat > 3 and n % 14 in [4, 8, 12]:
        print(f'tu+ru*{repeat+1}')
    else:
        print(ans + 'ru'*repeat)
else:
    print(ans)