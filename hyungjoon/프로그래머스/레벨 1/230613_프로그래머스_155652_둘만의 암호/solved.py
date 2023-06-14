def solution(s, skip, index):
    words = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        words = words.replace(i, '')
    
    answer = ''
    for i in s:
        start = words.index(i)
        # skip한 리스트 만큼 나머지연산 해주는것이 포인트
        end = (start + index) % len(words)
        answer += words[end]

    return answer

solution('aukks',"wbqd",5)
