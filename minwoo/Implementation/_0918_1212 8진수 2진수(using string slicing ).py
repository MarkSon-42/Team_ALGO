# 이건 좀 어렵다. 디버거를 찍어보면서 보는데, while, if로 저렇게 로직을 나누는걸 떠올리는게..
# while if while if ... bad.

n = input()

answer = ''

for i in range(len(n)):
    number = int(n[i])

    tmp = ''


    while number != 0:
        tmp += str(number % 2)
        number //= 2

    if i != 0:
        while len(tmp) < 3:  # 8진수는 111까지 3자리 이므로~
            tmp = tmp + '0'

    answer += tmp[::-1]

if not answer:
    print(0)
else:
    print(answer)