def solution(n):
    answer = int(toThree(n), 3)
    
    return answer

def toThree(n):
    temp = ''
    while n > 0:
        a = n // 3
        b = n % 3
        n = a
        temp += str(b)

    return temp

solution(45)