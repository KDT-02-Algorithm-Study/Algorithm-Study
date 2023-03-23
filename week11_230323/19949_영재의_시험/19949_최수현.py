# PyPy로 123004 KB, 1412 ms ㅠㅠㅠ
import sys
input = sys.stdin.readline

def generator(my_answer=list):
    global cases

    l = len(my_answer)
    if l == 10:
        cnt = 0
        for i in range(10):
            if my_answer[i] == answer[i]:
                cnt += 1
        if cnt >= 5:
            cases += 1
        return
    
    if l > 1 and my_answer[-1] == my_answer[-2]:
        for i in range(1, 6):
            if i == my_answer[-1]:
                continue
            else:
                my_answer.append(i)
                generator(my_answer)
                my_answer.pop()
    else:
        for i in range(1, 6):
            my_answer.append(i)
            generator(my_answer)
            my_answer.pop()

answer = list(map(int, input().split()))
cases = 0
generator([])
print(cases)