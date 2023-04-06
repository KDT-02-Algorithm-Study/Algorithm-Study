# 31256 KB / 40 ms
import sys
input = sys.stdin.readline

vowel = {'a', 'e', 'i', 'o', 'u'}
while 1:
    password = input().rstrip()
    if password == 'end':
        break
    
    # 모음, 자음 연속된 길이 카운트, 1로 시작
    cnt = 1
    is_impossible = False
    if password[0] in vowel:
        is_vowel = True
        include_v = True
    else:
        is_vowel = False
        include_v = False

    for i in range(1, len(password)):
        # e, o 가 아닌데 두번 연속된 알파벳은 종료
        if (password[i] == password[i-1]) and (password[i] not in {'e', 'o'}):
            is_impossible = True
            break
        
        # 모음인 경우
        if password[i] in vowel:
            # 모음 포함 O
            include_v = True
            # 앞에가 모음이었으면 cnt + 1
            if is_vowel:
                cnt += 1
            # 자음이었으면 cnt = 1로 초기화
            else:
                cnt = 1
            # 모음 표시
            is_vowel = True

        # 자음인 경우
        else:
            # 앞에가 모음이었으면 cnt = 1로 초기화
            if is_vowel:
                cnt = 1
            # 자음이었으면 cnt + 1
            else:
                cnt += 1
            # 자음 표시
            is_vowel = False
        
        # 세번 연속 자음/모음 나온 경우 break
        if cnt == 3:
            is_impossible = True
            break
    
    if include_v and not is_impossible:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')