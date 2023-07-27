# 효율성 테스트 3, 4번 시간초과

def solution(phone_book):
    # 길이 순서로 정렬해서 짧은 것부터 비교하는 식으로 진행
    phone_book.sort(key = lambda x : len(x))
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] in phone_book[j][:len(phone_book[i])]:
                return False
    return True