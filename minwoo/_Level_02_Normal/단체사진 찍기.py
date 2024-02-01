from itertools import permutations


def check_condition(opr, num, diff):
    if opr == '=':
        return num == diff
    elif opr == '>':
        return diff > num
    else:
        return diff < num


def solution(n, data):
    answer = 0
    friends = "ACFJMNRT"
    friends = [''.join(p) for p in permutations(friends)]

    for friend in friends:
        check = True
        for text in data:
            first_idx = friend.find(text[0])
            second_idx = friend.find(text[2])
            diff = abs(first_idx - second_idx) - 1
            num = int(text[4])

            if check_condition(text[3], num, diff):
                continue
            check = False
            break
        if check:
            answer += 1

    return answer