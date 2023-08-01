'''
문제 : 전화번호 목록
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577
'''
def solution(phone_book):
    # 1. 오름차순으로 정렬한다.
    phone_book.sort()
    
    # 2. int형으로 정렬하면 안된다. 문자열 순으로 정렬한 뒤에, 다음 인덱스의 n번째 까지만 비교해주면 된다.
    for i in range(len(phone_book) - 1):
        n = len(phone_book[i])
        if phone_book[i+1][:n] != phone_book[i]:
            return False
                
    return True
print(solution(["119", "97674223", "1195524421"]))