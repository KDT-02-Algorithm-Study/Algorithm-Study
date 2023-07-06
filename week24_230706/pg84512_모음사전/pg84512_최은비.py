# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    global answer
    answer = 0
    
    def recursion(tmp):
        global answer
        answer += 1
        
        if tmp == word:
            return True
        
        if len(tmp) == 5:
            return False
        
        for i in "AEIOU":
            flag = recursion(tmp+i)
            if flag:
                return True
    
    for i in "AEIOU":
        flag = recursion(i)
        if flag:
            break
                
    return answer