# ----------------------- [ enumerate() 내장 함수로 for문 돌리기 ]-----------------------
    # iterable을 순회하며 하나씩 프린트하되, 인덱스와 함께 출력하고 싶을 때 어떻게 해야 좋을까?


# < 틀린 방법은 아니지만 파이써닉 하지 않은 방법 1 >
    # 변수가 for 반복문이 종료된 이후에도 네임 스페이스에 남게 되서 별로인 코드
i = 0
for letter in ['A', 'B', 'C']:
    print(i, letter)
    i += 1



# < 틀린 방법은 아니지만 파이써닉 하지 않은 방법 2 >
    # 위의 방법보단 낫지만 파이썬 커뮤니티에서는 이러한 코드를 파이써닉하지 못하다고 함
letters = ['A', 'B', 'C']
for i in range(len(letters)):
    letter = letters[i]
    print(i, letter)



# < 파이써닉한 방법 : 내장 함수인 enumerate() 사용 >
    # enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 tuple을 만들어 줌
    # 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 unpacking(인자 풀기) 해줄 것
        # 일반 list를 iter() 함수에 넘겨 반복자(iterator)로 만든 후 next() 함수를 호출하여 순회

# case 1 : 튜플 형태로 출력
for entry in enumerate(['A', 'B', 'C']):
    print(entry)

    ## (0, 'A')
    ## (1, 'B')
    ## (2, 'C')

# case 2 : 인덱스와 원소를 각각 다른 변수로 출력
for i, letter in enumerate(['A', 'B', 'C']):
     print(i, letter)

    ## 0 A
    ## 1 B
    ## 2 C

# case 3 : 시작 인덱스 설정
for i, letter in enumerate(['A', 'B', 'C'], start = 101):
    print(i, letter)

    ## 101 A
    ## 102 B
    ## 103 C

# + case 4 : for문을 쓰지 않고 tuple의 형태로 (인덱스, 원소) 출력하기>>> enumerate_letters = enumerate(['A', 'B', 'C'])
enumerate_letters = enumerate(['A', 'B', 'C'])
next(enumerate_letters)
    ## (0, 'A')
next(enumerate_letters)
    ## (1, 'B')
next(enumerate_letters)
    ## (2, 'C')

# + case 5 : case 4의 경우를 list로 한번에 묶어주기
list(enumerate(['A', 'B', 'C']))
    ## [(0, 'A'), (1, 'B'), (2, 'C')]


# .
# .
# .
# .
# .


# < enumerate() 활용해보기 연습 - 이중 배열을 인덱스 붙여 원소 출력해보기 >

# 예시로 주어진 자료
matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

# 일반적으로 흔히들 작성하는 파이써닉하지 못한 방법으로 인덱스와 원소 출력하기
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(r, c, matrix[r][c])

    ## 0 0 A
    # 0 1 B
    # 0 2 C
    # 1 0 D
    # 1 1 E
    # 1 2 F
    # 2 0 G
    # 2 1 H
    # 2 2 I

#  enumerate()를 사용하여 파이써닉하게 코드 짜보기
for r, row in enumerate(matrix):
    for c, letter in enumerate(matrix[r]):
        print(r, c, letter)

    # 0 0 A
    # 0 1 B
    # 0 2 C
    # 1 0 D
    # 1 1 E
    # 1 2 F
    # 2 0 G
    # 2 1 H
    # 2 2 I
