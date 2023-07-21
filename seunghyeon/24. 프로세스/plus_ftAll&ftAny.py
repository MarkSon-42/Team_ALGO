# -------------------- [ 내장 함수 all(), any()에 대하여 ] --------------------



# < all() >
    # iterable의 모든 요소가 True거나 인자로 받은 요소가 비어있으면 True를 반환하는 함수

# 리스트 ex 1 : 일반적 상황
a = [1, 2, 3, 4, 5]
rst = all(a)
print(f'all([1, 2, 3, 4, 5]) : {rst}')
    ## all([1, 2, 3, 4, 5]) : True

# 리스트 ex 2 : 리스트 요소에 0(즉, False)가 있는 경우
b = [1,2,0,4,5]
print(f'all([1, 2, 0, 4, 5]) : {all(b)}')
    ## all([1, 2, 0, 4, 5]) : False

# 리스트 ex 3 : 리스트가 비어있는 경우
c = []
print(f'all([]) : {all(c)}')
    ## all([]) : True

# 문자열 ex 1 : 일반적 상황
d = 'textForTest'
print(f'all(\'textForTest\') : {all(d)}')
    ## all('textForTest') : True

# 문자열 ex 2: 비어있는 문자열인 경우
e = ''
print(f'all(\'\') : {all(e)}')
    ## all('') : True

# 튜플, 딕셔너리도 똑같다!


# .
# .
# .
# .
# .


# < any() >
    # iterable의 모든 요소에 하나라도 True가 있으면 True를 반환하는 함수

# ex 생략, all() 예시 참고하여 생각해보기
