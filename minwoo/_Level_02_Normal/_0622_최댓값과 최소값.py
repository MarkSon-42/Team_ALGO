# 공백으로 구분

# 이 문제는 많은 버전의 풀이를 다 숙지하는것이

# 학습의 핵심인듯 하다.

# 사람 생각이 다 비슷해서 나도 첫번째 풀이를 떠올렸지만 다른 풀이도 다 참고할만 함.
def solution(s):
    lst = list(map(int, s.split(' ')))
    return str(min(lst)) + " " + str(max(lst))


def solution_1(s):
    answer = ''
    arr = list(map(lambda x: int(x), s.split(' ')))
    arr.sort()
    answer = str(min(arr)) + ' ' + str(max(arr))
    return answer



def solution_2(s):
    answer = ''
    arr = list(map(lambda x: int(x), s.split(' ')))
    answer = str(min(arr)) + ' ' + str(max(arr))
    return answer


def solution_3(s):
    result = []
    num_list = [int(n) for n in s.split()]
    result.append(str(min(num_list)))
    result.append(str(max(num_list)))
    return ' '.join(result)

def solution_4(s):
    a = s.split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return str(min(a))+" "+str(max(a))