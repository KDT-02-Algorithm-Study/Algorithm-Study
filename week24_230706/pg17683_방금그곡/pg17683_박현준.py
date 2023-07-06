def change_music(music):
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'A#' in music:
        music = music.replace('A#', 'a')
    return music
def solution(m, musicinfos):
    answer = []
    for index, info in enumerate(musicinfos):
        temp = info.split(',')
        
        start_time = list(map(int, temp[0].split(':')))
        end_time = list(map(int, temp[1].split(':')))
        name = temp[2]
        music = change_music(temp[3])
        music_length = len(music)
        
        music_playtime = (end_time[0] * 60 + end_time[1]) - (start_time[0] * 60 + start_time[1])
        played_music = music * int(music_playtime / music_length) + music[:music_playtime%music_length]
        if change_music(m) in played_music:
            answer.append([music_playtime, index, name])
            
    answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    
    if not answer:
        return "(None)"
    else:        
        return answer[0][2]