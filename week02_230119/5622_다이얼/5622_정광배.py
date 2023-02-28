# 5622 다이얼

# WA 입력시 W(index(7)+3 ) + A(index(0)+3 ) = 13

datas = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
nums = input()

result = 0
for data in datas:
    for num in nums:
        if num in data:
            result += datas.index(data) + 3
print(result)