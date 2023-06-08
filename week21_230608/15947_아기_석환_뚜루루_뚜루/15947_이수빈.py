# 15947 아기 석환 뚜루루 뚜루
# 31256 KB / 44 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

lycs = 'baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan'
lycs = list(lycs.split())
len_lycs = len(lycs)

n = int(input())
n1 = int(n/len_lycs)
n2 = n % len_lycs -1

if lycs[n2] == 'turu' or lycs[n2] == 'tururu':
    res = str(lycs[n2]) +('ru'*n1)
    res_count = res.count('ru')
    if res_count >=5 :
        print(f'tu+ru*{res_count}')
    else :
        print(res)

else :
    print(lycs[n2])
