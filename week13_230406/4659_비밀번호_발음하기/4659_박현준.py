# 31256 KB / 44 ms

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = [chr(i) for i in range(97, 123) if chr(i) not in vowel]

def is_accep(PW):
    print(f'<{PW}> is acceptable.')
def is_not_accep(PW):
    print(f'<{PW}> is not acceptable.')

def check_first(PW):
    cnt = 0
    for v in vowel:
        if v in PW:
            cnt += 1
    if cnt == 0:
        return False

def check_second(PW):
    for c in range(len(PW)-2):
        if PW[c] in vowel and PW[c+1] in vowel and PW[c+2] in vowel:
            return False
        elif PW[c] not in vowel and PW[c+1] not in vowel and PW[c+2] not in vowel:
            return False

def check_third(PW):
    for c in range(len(PW)-1):
        if PW[c] == PW[c+1]:
            if PW[c] == 'e' or PW[c] =='o':
                continue
            else:
                return False

def check_validation(PW):
    if check_first(PW) == False or check_second(PW) == False or check_third(PW) == False:
        return False

while True:
    PW = input()
    if PW == 'end':
        break
    if check_validation(PW) == False:
        is_not_accep(PW)
    else:
        is_accep(PW)