def solution(N, number):
    answer = 0
    if N == number:
        return 1

    # 1. [set * 8 ] 초기화
    s = [set() for x in range(8)]
    # s[0] = {}, s[1] = {}
    # 2. 각 set마다 기본 수 "N" * i수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    print(i, x)  # 디버거 찍어보기 : 5, 55, 555, 5555, .. , 55555555

    # 3. N 일반화
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break

    else:
        answer -= 1

    return answer

solution(5, 12)