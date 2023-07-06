# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def time_convert(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m


# 샵이 붙은 음을 다른 문자로 치환
def sharp_convert(note):
    sharp = {"C#": "H", "D#": "I", "F#": "J", "G#": "K", "A#": "L"}
    for j in range(len(note)-1):
        if j + 1 > len(note) - 1:
            return note

        tmp = note[j]+note[j+1]
        if tmp in sharp:
            note = note.replace(tmp, sharp[tmp])
            
    return note


def solution(m, musicinfos):
    answer = ''
    musics = []
    m = sharp_convert(m)
    
    for i in range(len(musicinfos)):
        start, end, name, note = musicinfos[i].split(",")
        # 음악의 재생시간
        time = time_convert(end) - time_convert(start)
        note = sharp_convert(note)
                
        # 음악 재생시간이 악보보다 짧으면 재생한 만큼을 따로 저장
        if time < len(note):
            playing = note[:time]
        # 재생시간이 악보보다 길면 악보를 이어붙여서 재생시간만큼 늘려주기
        else:
            playing = note * (time//len(note)) + note[:(time%len(note))]

        # 멜로디가 겹치면 [재생시간, 곡 이름] 형식으로 리스트에 저장
        if m in playing:
            musics.append([time, name])

    # 겹치는 음악이 없을 경우
    if not musics:
        answer = "(None)"
    else:
        # 가장 긴 재생시간을 따로 저장하고 출력
        max_playing = max(musics, key=lambda x: x[0])[0]
        
        for time, name in musics:
            if time == max_playing:
                answer = name
                break
        
    return answer