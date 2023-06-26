def ftToBin(num):
    return str(bin(num)[2:]).count('1')

def solution(n):
    answer = 0
    tmpN = n + 1
    while (1):
        if ftToBin(n) == ftToBin(tmpN):
            answer = tmpN
            break
        tmpN += 1
            
    return answer
