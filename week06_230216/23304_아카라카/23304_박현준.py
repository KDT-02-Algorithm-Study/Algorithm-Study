def pellin(S):
    if len(S) == 1:
        return True
    half = int(len(S) / 2)
    if len(S) & 1:
        S1 = S[:half]
        S2 = S[half+1:]
    else:
        S1 = S[:half]
        S2 = S[half:]
    if S1 != S2:
        return False
    if pellin(S1) & pellin(S2):
        return True
    return False
S = input()
if pellin(S):
    print('AKARAKA')
else:
    print('IPSELENTI')