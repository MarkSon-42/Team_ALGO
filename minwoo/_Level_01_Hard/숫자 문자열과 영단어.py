# 뭔가 비슷한 유형의 문제를 풀었던거 같다. 숫자와 단어, 그러니까 정수형 자료형과 문자열 자료형이 1:1로 대응하는 데이터를 제시하는 문제
# 파이썬으로 요일문제?를 푼것에서 딕셔너리를 사용했던거 같은데, 주어진 대응표를 딕셔너리로 선언하는것을 시작으로 문제풀이 시도. .
# 입력받는 문자열 s에서 숫자는 제외하고 문자열만 딕셔너리에 대응하는 숫자로 변환해서 출력해주면 된다.
# 반복문 ㄱ
# 생각해보니, s에 있는 숫자는 정수가 아니라 정수모양인 문자일 뿐이다. 그래서 변환을 해줘야 함.
# -> 그럴 필요 없음. 그냥 딕셔너리 일치하는것만 숫자 모양으로 바꿔주고,
#
# 출력을 정수로 바꿔서 출력하면 된다.


def solution(s):
    # n_words = {0 :'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four',
    #            5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight',  9 : 'nine' }
    # -> 이럴게 아니라,

    num_words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    # 근데 key, value의 자료형은 상관이 없나? -> 안됨.

    answer = s

    # items()를 쓰자. 딕셔너리에 있는 키와 값의 쌍을 가져올 수 있음. 키는 key에 ,  값은  value에
    for key, value in num_words.items():
        answer = answer.replace(key, value)
    return int(answer)