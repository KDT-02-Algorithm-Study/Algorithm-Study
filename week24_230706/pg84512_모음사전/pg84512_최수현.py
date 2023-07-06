def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    ans = len(word)

    # word 앞에서부터 한자리씩 보면서 word이전에 나왔을 모든 단어 count
    # ex) word = 'I'
    for i in range(len(word)):
        n = vowels.index(word[i])   # n = 2
        ans += n                    # I앞에 A,E 2개가 있으므로 +2
        calc = n                    # 계산할 변수에 A,E 두가지 경우 2 저장
        for j in range(4-i):        # 현재 자리 문자 뒤에 붙이는 것이므로 5-i-1 -> 4-i
            calc *= 5               # A, E에 붙일 수 있는 문자 5가지이므로 곱하기 5
            ans += calc             # 지금 만든 문자의 경우의 수 ans에 더하기
            
    return ans

"""
ans에 word길이만큼을 담는 이유
ex) 'AAAAA'인 경우
'AAAAA'이전에 'A', 'AA', 'AAA', 'AAAA'가 있고 'AAAAA'까지 카운트하므로
"""