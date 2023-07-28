import math

def solution(n, k):
    
    current_number = n
    prime_count = 0
    # k진수로 바꾼 숫자 저장
    k_mod_number = ""
    
    # k진수 변환 과정
    while True:
        if current_number < k:
            k_mod_number = str(current_number) + k_mod_number
            break
            
        remainder = current_number % k
        k_mod_number = str(remainder) + k_mod_number
        current_number = current_number // k
        
    zero_count = k_mod_number.count("0")
    zero_index = []
    
    # 문자열에서 0이 있는 인덱스의 위치를 리스트에 저장
    for i in range(zero_count):
        if i == 0:
            index = k_mod_number.find("0", i)
        else:
            index = k_mod_number.find("0", zero_index[i - 1] + 1)
        zero_index.append(index)
    
    # 만약 k진수 변환 형태에 0이 없는 경우는 자체 연산
    if zero_count == 0:
        if is_prime(k_mod_number):
            prime_count += 1
    else:
        for i in range(len(zero_index)):
            if i == 0:
                if is_prime(k_mod_number[:zero_index[i]]):
                    prime_count += 1

            # zero_index의 마지막 숫자인 경우 마지막도 같이 연산해주어야함
            elif i == len(zero_index) - 1:
                if is_prime(k_mod_number[zero_index[i - 1] + 1:zero_index[i]]):
                    prime_count += 1
                if is_prime(k_mod_number[zero_index[i] + 1:]):
                    prime_count += 1
            else:
                if is_prime(k_mod_number[zero_index[i - 1] + 1:zero_index[i]]):
                    prime_count += 1

    return prime_count


def is_prime(number):
    if number == "1":
        return False
    elif number == "":
        return False
    else:
        number = int(number)
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
        return True