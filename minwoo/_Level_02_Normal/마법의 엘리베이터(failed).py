# 거꾸로 올라갔다가 내려가는 방법이나
# 그대로 내려가는 방법
# 이 두가지 중에 최소 방법을 리턴하는
# 방식을 사용하면 될듯?
# storey의 마지막 자릿수 숫자가 6이상이나 아니냐가 관건인듯?

# 테케 통과인데 제출해보면 30점..

# .. 아님!!

def solution(storey):
    answer = 0
    storey = str(storey)
    ev = int(storey[-1:])
    magic = storey[:-1]
    if ev >= 6:
        magic = str(int(magic) + 1)
        reverse = 10 - ev
        for m in magic:
            answer += int(m)
        answer += reverse
    else:
        answer += ev
        for m in magic:
            answer += int(m)
    return answer

