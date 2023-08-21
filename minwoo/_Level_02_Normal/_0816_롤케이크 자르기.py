# 자료구조나 어떤 메서드를 쓰는게 맞는거 같은데..(LV 2 50%)
# len(set()) -> X

def solution(topping):
    answer = 0
    dic_left = dict()
    dic_right = dict()
    for i in topping:
        if dic_right.get(i) == None:
            dic_right[i] = 1
        else:
            dic_right[i] += 1


# 이 풀이 no

