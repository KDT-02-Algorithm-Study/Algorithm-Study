# 방금그곡
# 테스트 29 〉	통과 (1.27ms, 10.5MB)
 
def replace_code(s):
    return s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

def change_time(h, m):
    return h*60+m

def solution(m, musicinfos):
    answer = '(None)'
    m = replace_code(m)
    l = 0
    for i in musicinfos:
        start, end, song, code = i.split(',')
        s_h, s_m = map(int, start.split(':'))
        e_h, e_m = map(int, end.split(':'))
        start = change_time(s_h, s_m)
        end = change_time(e_h, e_m)
        now_l = end - start
        code = replace_code(code)
        code = code*(now_l//len(code))+code[:now_l%len(code)] # 재생 길이만큼 code 늘려주기
        if m in code and l < now_l:
            answer = song
            l = now_l
    return answer