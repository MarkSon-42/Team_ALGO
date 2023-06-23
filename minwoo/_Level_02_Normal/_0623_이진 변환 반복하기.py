def solution(s):

    zero_cnt = 0
    trans_cnt = 0

    while s != '1':
        zero_cnt += s.count('0')

        s = s.replace('0', '')
        str_len = len(s)

        s = str(format(str_len, 'b'))
        trans_cnt += 1

    return [trans_cnt, zero_cnt]



def solution_01(s):
    a, b = 0, 0

    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]



from collections import Counter
def solution_02(s):
    cnt, zero = 0, 0
    while s != '1':
        cnt += 1
        counter = Counter(s)
        zero += counter['0']
        s = bin(counter['1'])[2:]
    return [cnt, zero]
