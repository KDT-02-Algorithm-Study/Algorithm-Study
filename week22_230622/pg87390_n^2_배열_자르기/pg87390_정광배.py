# n^2 배열 자르기
# 테스트 19 〉	통과 (962.33ms, 397MB)

def solution(n, left, right):
    answer = []
    # left
    a = left//n
    aa = left%n
    # right
    b = right//n
    bb = right%n

    # 같은 행일 때
    if a == b:
        c = [i+1 if i > a else a+1 for i in range(n)]
        answer = c[aa:bb+1]
    # 다른 행일 때
    else:
        answer += [i+1 if i > a else a+1 for i in range(n)][aa:]
        for j in range(a+1, b):
            answer += [i+1 if i > j else j+1 for i in range(n)]
        answer += [i+1 if i > b else b+1 for i in range(n)][:bb+1]
    return answer


# 시간초과
# 모든 배열을 미리 만들어 놓음

# def solution(n, left, right):
#     answer = []
#     a = left//n
#     aa = left%n
#     b = right//n
#     bb = right%n
#     d = [[i+1 if i > j else j+1 for i in range(n)] for j in range(n)]
#     if a == b:
#         answer = d[a][aa:bb+1]
#     else:
#         answer += d[a][aa:]
#         for i in range(a+1, b):
#             answer += d[i]
#         answer += d[b][:bb+1]
#     return answer

# print(solution(3, 2, 5))
'''
1 2 3
2 2 3
3 3 3
'''
# print(solution(4, 7, 14))
'''
1 2 3 4
2 2 3 4
3 3 3 4
4 4 4 4
'''