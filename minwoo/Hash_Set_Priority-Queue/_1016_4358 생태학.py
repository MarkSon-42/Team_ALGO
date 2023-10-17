# 1. 10,000개의 종에 1,000,000그루가 주어진다
# 2. dict를 써야할 것이다.
# 3. 종 이름만 사전순으로 출력하면 된다



# 10.17.... python 기초를 계속 까먹는다.... 코드 전 라인에 주석 달고
# 코드 다 지우고 주석보면서 처음부터 다시짜는 연습을 해야할 듯 ( 대단히 심각 )
import sys

# 표준 입력에서 한 줄씩 읽기 위해 sys.stdin.readline을 사용
input = sys.stdin.readline

# 전체 나무 수를 저장할 변수를 초기화
total_size = 0

# 나무 종 이름과 그 수를 저장할 딕셔너리 생성 (키 : 이름, 값 : 카운트)
tree_name = {}

# 더 이상 입력이 안될때까지 입력받기 - 조건문 유의
while True:
    name = input().rstrip()  # 여기서 rstrip()을 쓰는 이유.. 디버거 돌려보면
    # readline때문에 나무이름 뒤에 \n까지 입력받는데 이를 날려줘야 한다.
    if name == '':  # 아무것도 주어지지 않으면 break
        break
    total_size += 1  # 입력 받는 개수를 세주기 ( 전체 개수를 알아야 어떤 종이 몇 %인지 알 수 있음 )
    if name in tree_name:
        tree_name[name] += 1
    else:
        tree_name[name] = 1
sorted_tree_name = dict(sorted(tree_name.items()))  # 이렇게 하면 키값으로 사전순 정렬

for i in sorted_tree_name:
    tmp = sorted_tree_name[i]
    per = ((tmp / total_size) * 100)


# 이름과 문자를 소수점 넷째짜리 까지 출력.
    print("%s %.4f" % (i, per))