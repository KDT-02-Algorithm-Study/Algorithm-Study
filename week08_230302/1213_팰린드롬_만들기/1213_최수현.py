# 메모리 31256 KB, 시간 48 ms
import sys
intput = sys.stdin.readline

name = input().rstrip()
pal = {}

# 알파벳과 그 수를 딕셔너리로 저장
for n in name:
    if n in pal:
        pal[n] += 1
    else:
        pal[n] = 1

odd = 0
center = ''
pal_name = ''
for k, v in sorted(pal.items()):
    # 홀수인 알파벳은 가운데 글자로 지정
    if v & 1:
        odd += 1
        center = k
        # 홀수인게 두개 이상이면 break
        if odd > 1:
            print("I'm Sorry Hansoo")
            break
    pal_name += k * (v//2)
else:
    print(pal_name, center, pal_name[::-1], sep='')