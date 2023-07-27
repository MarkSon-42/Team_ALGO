# 해시

# 리스트를 통해서 접근하면 시간초과가 날 것임

# 접두어 ->  sort()? -> 접두어가 있기만 한다면 false리턴하고 종료.

def solution(phone_book):
    answer = True
    phone_book.sort()
    # 접두어기때문에 글자수 작은것 앞에서부터 슬라이싱 비교를 들어가면 된다.
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer

# python에서 이렇게 하면 100% 시초날듯.. phone_book길이 1,000,000
# 근데 통과됨.. (?)

# using hash
def solution2(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True


print(solution(["6", "12", "6789"]))