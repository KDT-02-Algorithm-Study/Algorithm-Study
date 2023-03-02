def check():
    global mid, cnt
    for k, v in dic.items():
        if v & 1:
            cnt += 1
            mid = k
            if cnt >= 2:
                print("I'm Sorry Hansoo")
                return False
    return True

name = [x for x in input()]
name.sort()
dic = {}
left = ''
cnt = 0
mid = ''
for c in name:
    dic[c] = dic.get(c, 0) + 1
if check():
    for k, v in dic.items():
        left += (k * (int(v/2)))
    right = left[::-1]
    print(left + mid + right)