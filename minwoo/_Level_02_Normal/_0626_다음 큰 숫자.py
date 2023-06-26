def solution(n):
    # 1. n을 이진수로 변환한 뒤 1의 개수를 센다.
    bin_n = bin(n)[2:]  # 이진수로 변환 후 "0b" 제거 -> bin()은 int를 받아서 이진수(문자열)로 나타내줌...!!
    count_n = bin_n.count('1')

    # 2. n보다 큰 숫자들 중에서 위에서 구한 1의 개수와 같은 개수의 1을 가진 수를 찾는다.
    next_num = n + 1
    while True:
        bin_next = bin(next_num)[2:]  # 이진수로 변환 후 "0b" 제거
        cnt_next = bin_next.count('1')
        if cnt_next == count_n:
            return next_num
        next_num += 1



# while True이지만 n이 1,000,000밖에 안되는데다가
# bin()

# https://stackoverflow.com/questions/50793388/time-complexity-of-bin-in-python