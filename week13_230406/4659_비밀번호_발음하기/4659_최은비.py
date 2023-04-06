# 비밀번호 발음하기 https://www.acmicpc.net/problem/4659
# 31256KB / 44ms
import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    flag = True

    if s == 'end':
        break
    
    # 1. 모음을 하나 이상 포함하는지
    for ch in s:
        if ch in 'aeiou':
            break
    else:
        print(f"<{s}> is not acceptable.")
        flag = False
        continue
    
    # 2. 모음, 자음이 3개 이상 연속으로 오는지
    for i in range(len(s)-2):
        # 2-1. 모음이 세개 이상인 경우를 판단
        if s[i] in 'aeiou':
            for j in range(3):
                if s[i+j] in 'aeiou':
                    flag = False
                else:
                    flag = True
                    break
            
            if not flag:
                print(f"<{s}> is not acceptable.")
                break
        # 2-2. 자음이 세개 이상인 경우를 판단
        else:
            for j in range(3):
                if s[i+j] in 'aeiou':
                    flag = True
                    break
                else:
                    flag = False
            
            if not flag:
                print(f"<{s}> is not acceptable.")
                break
    
    # 3. oo와 ee를 제외한 같은 글자가 연속으로 두번 나오는지
    for i in range(len(s) - 1):
        if s[i] not in 'eo':
            if s[i] == s[i+1]:
                print(f"<{s}> is not acceptable.")
                flag = False
                break
    
    # 위에 조건에서 걸러지지 않은 단어는 acceptable
    if flag:
        print(f"<{s}> is acceptable.")