def solution(s):
    lst = s.split(' ')
    temp = []
    for i in lst:
        i = i.capitalize()
        temp.append(i)
    return ' '.join(temp)
