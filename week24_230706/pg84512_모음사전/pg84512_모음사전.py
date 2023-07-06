# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 1.23ms, 10.3MB / 2.50ms, 10.3MB

'''
# 문제 이해
- 알파벳 순서와 길이에 따라 순서가 결정됨 
- 'A', 'E', 'I', 'O', 'U' 로 만들 수 있는 모든 경우의 수를 판단 

# 문제 해석 
- word 길이는 1이상 5이하 -> 중복순열로 모든 조합을 계산하고, index로 찾기

'''
 
from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i): # 1에서 5개까지 모든 조합을 구함
            words.append(''.join(list(j))) # 하나의 단어로 

    words.sort() # 정렬
    # 그 이후 index를 사용하여 찾기 
    res = words.index(word) + 1
    return res
