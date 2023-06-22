def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        # 몫과 나머지가 인덱스
        a, b = divmod(i, n)
        # 둘 중에 큰 것+1이 배열의 값이 됨
        answer.append(max(a, b)+1)

    return answer


# # 시간초과
# def solution(n, left, right):
#     matrix = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(i+1):
#             matrix[i][j] = i+1
#             matrix[j][i] = i+1

#     arr = []
#     for line in matrix:
#         arr += line

#     answer = arr[left:right+1]
#     return answer