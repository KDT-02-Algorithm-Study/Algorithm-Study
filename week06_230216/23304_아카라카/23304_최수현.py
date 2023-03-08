import sys
sys.setrecursionlimit(10**6)

def palindrome(s):
    is_pal = False
    l = len(s)

    if l == 1:
        is_pal = True
        return is_pal
    
    if s == s[::-1]:
        is_pal = palindrome(s[:l//2])
    
    return is_pal

s = sys.stdin.readline().rstrip()
if palindrome(s):
    print('AKARAKA')
else:
    print('IPSELENTI')