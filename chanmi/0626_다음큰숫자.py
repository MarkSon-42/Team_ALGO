def solution(n):
    bin_num = str(bin(n))
    bin_num = bin_num.replace("0b", "")
    one_count = bin_num.count("1")
    test_num = int(bin_num, 2)
    print(bin_num)
    while True:
        test_num2 = str(bin(test_num)).replace("0b", "")
        test_count = test_num2.count("1")
        if one_count == test_num2.count("1") and test_num != int(bin_num, 2):
            break
        else:
            test_num += 1
    answer = test_num
    return answer