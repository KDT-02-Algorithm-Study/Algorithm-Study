# https://school.programmers.co.kr/learn/courses/30/lessons/17683
# 0.03ms, 10.3MB / 1.70ms, 10.3MB

'''
# 문제 이해
- #이 있고 없고의 차이를 구분해줘야함 
- 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생
- 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생
- 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.

# 문제 해석
- # 차이 구분해주기 위해 replace 활용 (소문자로)
- 음악이 시작, 끝난, 음악 정보, 악보 정보 등을 구분자로 분리해야함
- 조건에 맞춰서 포함되는지 안 되는지 변경
- .. 어렵.. 

'''

def replace_code(cc):
    cc = cc.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    return cc

def solution(m, musicinfos):
    res = []

    for musicinfo in musicinfos: # 구분자로 분리하여 각각 저장
        info = musicinfo.split(',')
        start = info[0].split(':')
        end = info[1].split(':')
        
        # 재생 시간 구하기고, 네오가 기억한 멜로디로 바꾸고
        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1]) 
        code = replace_code(info[3])
        # 재생 시간만큼의 코드 구하기
        code = code * (time // len(code)) + code[:time%len(code)]
        
        # 네오가 기억하는 멜로디가 구한 코드에 포함되는지 확인 
        if replace_code(m) in code:
            res.append([info[2], time])

    if len(res) == 0:
        return "(None)" # 후보군에 없을 시 '(None)' 반환
    
    else:
        res = sorted(res, key = lambda x: (-x[1])) # 재생된 시간과, 입력된 순서 기준으로 정렬
        return res[0][0] 
