import sys

s = sys.stdin.readline()
ord_s = list(map(ord, s))

for i in range(len(ord_s)):
    if (64 < ord_s[i] < 91):
        ord_s[i] += 13
        if ord_s[i] > 90:
            ord_s[i] -= 26
    elif (96 < ord_s[i] < 123):
        ord_s[i] += 13
        if ord_s[i] > 122:
            ord_s[i] -= 26

chr_s = list(map(chr, ord_s))
print(''.join(chr_s))
