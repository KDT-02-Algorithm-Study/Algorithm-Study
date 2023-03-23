# 19949 영재의 시험
# 31256 KB / 2652 ms

def check(nums, point):
    global result
    l = len(nums)
    if nums and nums[-1] == answer[l-1]: # 방금 추가한 답이 정답일 때
        point += 1

    if l == 10: # 10문제 다 채웠을 때
        if point >= 5: # 5점이상이면 result += 1
            result += 1
        return

    for j in range(1, 6): # 1, 2, 3, 4, 5 # 5지 선다
        if l >= 2 and nums[-2] == nums[-1] == j: # 3연속 같은 답을 적었을 때
            continue
        nums.append(j)
        check(nums, point)
        nums.pop() # 백트래킹

answer = list(map(int, input().split()))
result = 0
check([],0)
print(result)


# 영재의 시험 간략화
# 3 지선다
# 3 문제
# 2점 이상
# 같은 수 연속 2개 이상 x
'''
1 1 1  / 2 1 1  / 3 1 1 
1 1 2  / 2 1 2  / 3 1 2 
1 1 3  / 2 1 3  / 3 1 3
  
1 2 1  / 2 2 1  / 3 2 1 
1 2 2  / 2 2 2  / 3 2 2 
1 2 3  / 2 2 3  / 3 2 3 
  
1 3 1  / 2 3 1  / 3 3 1 
1 3 2  / 2 3 2  / 3 3 2 
1 3 3  / 2 3 3  / 3 3 3 
'''

# 1 2 1 / 1 2 3 / 1 3 1 / 1 3 2 / 
# 2 1 2 / 2 1 3 / 2 3 1 / 2 3 2 /
# 3 1 2 / 3 1 3 / 3 2 1 / 3 2 3

# 답이 1 2 2 일 때 출력은 1 2 1, 1 2 3, 1 3 2 => 3


# def per(c, p):
#     global r
#     if c and c[-1] == d[len(c)-1]:
#         p += 1
#     if len(c) == 3: # 3문제
#         if p >= 2: # p가 2 이상일 때
#             r += 1
#             print(c, p)
#         return
    
#     for i in range(1, 4): # 3지선다
#         if c and c[-1] == i: # len(c) > 0
#             continue
#         c.append(i)
#         per(c, p)
#         c.pop()
#     p -= 1

# d = [1, 2, 2]
# r = 0
# per([], 0)
# print(r)