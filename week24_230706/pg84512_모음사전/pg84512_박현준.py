def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    dict = []
    def find_dict(index, word):
        if index == 5:
            return
        for i in range(5):
            temp = word + words[i]
            dict.append(temp)
            find_dict(index + 1, word + words[i])
    find_dict(0, '')
    answer = dict.index(word) + 1
    return answer