def solution(phone_book):
    phone_book.sort()  # 정렬
    phone_dict = {phone: 1 for phone in phone_book}  # 해시맵 생성
    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i + 1][:length]:  # 접두사 확인
            return False
    return True