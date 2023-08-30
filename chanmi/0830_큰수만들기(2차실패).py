from itertools import combinations

def solution(number, k):
    # k만큼 작은 숫자를 빼주기로 함
    # 만약 동일할 경우, 앞에서부터 숫자 제거
    
    # 숫자 종류 체크
    number_var = list(set(number))
    number_var.sort()
    print(number_var)
    count = 0
    index = 0
    number_list = list(number)

    print(number_list)
    
    while count < k:
        number_count = number_list.count(number_var[index])
        print("count :", count, ", number_count :", number_count)
        # number_var[index]에 해당하는 숫자가 있는 경우
        if number_count != 0:
            number_index = number_list.index(number_var[index])
            number_list.remove(number_list[number_index])
            print(number_list)
            count += 1
        
        # count가 0인 경우
        else:
            if index < len(number_var):
                index += 1
                continue
            else:
                break
    print(''.join(number_list))
            
    return str(''.join(number_list))