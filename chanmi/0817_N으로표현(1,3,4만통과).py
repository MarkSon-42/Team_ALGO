def solution(N, number):
    # N으로 number을 표현하기...
    
    # N을 한 번 사용하는 경우(1) : N
    # N을 두 번 사용하는 경우(1 + 4) : NN, N + N, N * N, N - N, N / N
    # N을 세 번 사용하는 경우(1 + 4 + 4 * 4) : NNN, NN + N, NN - N, NN * N, NN / N, N + (N + N), N + (N * N), ...
    
    if N == 1:
        if number == N:
            return 1
        
    # N이 2보다 큰 경우
    else:
        i = 2
        number_list = [N]
        
        while True:
            
            number_len = len(number_list)
            continuous_number = int(str(N) * i)
            
            if continuous_number == number:
                return i
            else:
                number_list.append(continuous_number)
                
            for j in range(number_len):
                if number == number_list[j] + N:
                    return i
                elif number == number_list[j] - N:
                    return i
                elif number == N - number_list[j]:
                    return i
                elif number == number_list[j] * N:
                    return i
                elif number == number_list[j] // N:
                    return i
                elif number_list[j] != 0 and number == N // number_list[j]:
                    return i
                else:
                    number_list.append(number_list[j] + N)
                    number_list.append(number_list[j] - N)
                    number_list.append(number_list[j] * N)
                    number_list.append(number_list[j] // N)
                    number_list.append(N - number_list[j])
                    if number_list[j] != 0:
                        number_list.append(N // number_list[j])
            
            for j in range(number_len):
                number_list.remove(number_list[0])
            # print(i, "일때 :", number_list)
            # print(len(number_list))
            i += 1
            
            if i >= 9:
                return -1
            
    return answer