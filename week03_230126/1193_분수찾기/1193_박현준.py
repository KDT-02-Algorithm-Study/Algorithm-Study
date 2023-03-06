N = int(input())
group = 0
start = 0
while 1:
    group += 1
    if N <= int(group * (group+1)/2):
        break
start = int(N - ((group-1)*group/2))
if group % 2 == 0:
    print(f'{start}/{group-start+1}')
else:
    print(f'{group-start+1}/{start}')