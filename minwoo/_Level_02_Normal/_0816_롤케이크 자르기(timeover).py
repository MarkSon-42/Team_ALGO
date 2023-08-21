

def solution(topping):
    answer = 0
    for i in range(1, topping):
        if len(set(topping[:i])) == len(set(topping[i+1:]))
            answer +=1
    return answer

