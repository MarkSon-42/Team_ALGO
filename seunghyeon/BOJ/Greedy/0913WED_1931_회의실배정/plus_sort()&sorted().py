# < .sort() & .sorted() >


# ex 1) .sort() 사용 -> sort()의 return 값이 None임을 주의! 정렬된 값은 리턴되지 않고 원본 list 값이 정렬된 값으로 수정되기만 함
a1 = [6, 3, 9]
print('a1:', a1)
a2 = a1.sort()
print('a1:', a1)
print('a2:', a2)

## [6, 3, 9]
## [3, 6, 9]
## None


# ex 2) .sorted() 사용
b1 = [6, 3, 9]
print('b1:', b1)
b2 = sorted(b1)
print('b1:', b1)
print('b2:', b2)

## b1: [6, 3, 9]
## b1: [6, 3, 9]
## b2: [3, 6, 9]