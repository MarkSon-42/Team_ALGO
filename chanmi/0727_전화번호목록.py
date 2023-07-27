def solution(phone_book):
    # 길이 순서가 아니라 오름차순으로 정렬
    # 이 경우 1 -> 2 -> 3 -> ...으로 정렬되기 때문에 만약 앞에서 접두어가 아니면 뒤쪽도 전부 아니게 됨
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] in phone_book[j][:len(phone_book[i])]:
                return False
            else:
                break
    return True