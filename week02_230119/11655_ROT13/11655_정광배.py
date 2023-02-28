# 11655 ROT13

S = input()
result = ''
for i in S:
    if i.islower(): # -97 + 13 = -84
        result += chr((ord(i)-84) % 26 + 97)
    elif i.isupper(): # -65 + 13 = -52
        result += chr((ord(i)-52) % 26 + 65)
    else:
        result += i
print(result)
