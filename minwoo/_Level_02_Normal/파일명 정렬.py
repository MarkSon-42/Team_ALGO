# 파일 숫자순 정렬 구현하기
# file = 'HEAD' + 'NUMBER' + 'TAIL'
# key(1) 정렬해야 하는듯?

# 기준

# 우선 HEAD 부분을 기준으로 사전 순으로 정렬
# 대소문자 구분을 하지 않는다 -> 전처리

# 첫 부분은 대소문자 구분 없이 Case Insensitive

# 다음 부분은 숫자 값에 따라 Numerical 정렬

# 정렬 기준에 따라 차이가 없다면 원래 입력에서 주어진 순서를 유지하는 안정 정렬 Stable Sort을 사용

# 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬

# 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지

# 입력 목록의 각 파일 이름에 대해, 세 개의 빈 문자열을 초기화합니다: head, number, tail. 이들은 파일 이름의 다른 부분을 저장

def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''
        # head, number, tail 분리해서 담아주기
        number_check = False

        for i in range(len(f)):
            if f[i].isdigit():
                number += f[i]
                number_check = True
            elif not number_check:
                head += f[i]
            else:
                tail = f[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))


    return [''.join(t) for t in answer]

