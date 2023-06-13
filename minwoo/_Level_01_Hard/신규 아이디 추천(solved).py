def solution(new_id):
    answer = ''
    # 규칙 1
    new_id = new_id.lower()
    # 규칙 2   isalpha() + isdigit() -> is isalnum()  오호라..
    for c in new_id:
        if c.isalnum() or c in "-_.":
            answer += c
    # 규칙 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 규칙 4
    if answer[0:1] == ".":
        answer = answer[1:]
    if answer[-1:0] == ".":
        answer = answer[-1]

    # 규칙 5
    if answer == '':
        answer = 'a'

    # 규칙 6 ( 자르고 나서 마지막에 '.' 이 있을 수 있음에 주의!!
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]


    # 규칙 7
    while len(answer) < 3:
        answer += answer[-1]

    return answer

