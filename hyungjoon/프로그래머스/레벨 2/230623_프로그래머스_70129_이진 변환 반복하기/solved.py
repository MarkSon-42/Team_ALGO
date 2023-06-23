def solution(s):
    answer = [0, 0]
    # s가 1이면 작업안해도됨
    if s == '1':
        return answer
    
    while True:
        temp = convertBin(s)
        # s 갱신 및 이진변환 횟수 증가
        s = temp[0]
        answer[0] += 1
        answer[1] += temp[1]
        if temp[0] == '1':
            break
    
    return answer

def convertBin(s):
    # 각각 0과 1
    removed = 0
    removed = s.count('0')
    s = s.replace('0', '')
    return (str(format(len(s), 'b')), removed)

solution("0111010")
