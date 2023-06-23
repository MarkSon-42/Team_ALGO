def solution(s):
    count = 0
    delete_zero = 0
    
    while(True):
        # 0을 모두 지워서 1만 남으면 무한 loop 정지
        if s == "1":
            break
            
        find_zero = s.find("0")
        num_length = 0
        
        # 0이 없는 경우
        if find_zero == -1:
            num_length = len(s)
            
            # 1만 남은 경우 정지
            if num_length == 1:
              break
            
            
            binary_num = ""
            while True:
                if num_length == 1:
                    binary_num = "1" + binary_num
                    print(binary_num)
                    break
                remainder = num_length % 2
                num_length = int(num_length / 2)
                print("나머지:", remainder)
                print("남은 길이:", num_length)
                binary_num = str(remainder) + binary_num
                print("이진변환:",binary_num)
            s = binary_num
            count += 1
        else:
            delete_zero += s.count("0")
            print("지워진 수 : ", s.count("0"))
            s = s.replace("0", "")
            
            num_length = len(s)
            print("길이 : " , len(s))
            binary_num = ""
            while True:
                if num_length == 1:
                    binary_num = "1" + binary_num
                    print(binary_num)
                    break
                remainder = num_length % 2
                num_length = int(num_length / 2)
                print("나머지:", remainder)
                print("남은 길이:", num_length)
                binary_num = str(remainder) + binary_num
                print("이진변환:",binary_num)
            s = binary_num
            count += 1            
    answer = [count, delete_zero]
    return answer