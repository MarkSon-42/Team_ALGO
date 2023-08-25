def solution(numbers):
    number = list(map(str, numbers))
    max_str = max(number, key=len)
    for i in range(1, len(max_str)):
        number.sort(key=lambda x: (x[0], x[i] if len(x) >= (i + 1) else x[-1]), reverse=True)
    print(number)
    answer = "".join(number)
    return answer