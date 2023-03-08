N = int(input())
cnt = 0
for _ in range(N):
    string = input()
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            continue
        elif string[i] in string[i+1:]:
            cnt += 1
            break
print(N-cnt)