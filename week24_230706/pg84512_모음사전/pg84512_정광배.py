# 모음사전
# 테스트 17 〉	통과 (0.11ms, 10.4MB)

from itertools import product

V = ['A','E','I','O','U']
words = []
for i in range(1, 6):
    for j in product(V, repeat=i):
        words.append(''.join(j))
words.sort() # 사전 순 정렬

def solution(word):
    answer = words.index(word)+1
    return answer