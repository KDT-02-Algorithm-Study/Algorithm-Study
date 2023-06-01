# 239312 KB / 540 ms

S = input()
dic = {}
S_length = len(S)
for i in range(S_length):
    for j in range(i, S_length):
        tmp = S[i:j+1]
        dic[tmp] = dic.get(tmp, 1) + 1
print(len(dic))