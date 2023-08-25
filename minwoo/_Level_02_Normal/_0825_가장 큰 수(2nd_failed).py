# 숫자의 길이를 늘려본다는 아이디어.. <- 근거가 무엇..?

# 두번째 테스트케이스에 힌트가 있다.
# [3, 30, 34, 5, 9] -> 9 5 34 3 30
# -> 3이 30보다 앞에온다 그리고 34보다는 뒤에있다
# 직관적으로 생각해보면 아리송한게 9, 5의 위치는 이해가 가지만 34 3 30 이 이상함.
# 결국 한자릿수가 들어가는 위치를 처리해야
# 그래서 숫자의 길이를 늘려준다.
# 그리고 원소의 길이가 1000이하이기 때문에 lambda x: x * 3으로 문자열 곱셈을 할 수 있다.
# 343434  333 303030 -> 자릿수를 비교하면
# 343 > 333 > 303

# []

def solution(numbers):
    str_numbers = sorted(list(map(str, numbers)), reverse=True, key=lambda x: x * 3)
    str_numbers = str(" ".join(str_numbers))
    return str_numbers.replace(" ", "")


# 11번 테케가 통과가 안된다. 하..