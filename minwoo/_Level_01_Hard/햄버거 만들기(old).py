# 예전에 푼 코드에 gpt를 통해서 상세한 주석을 추가함.

def solution(ingredients):
    need = 1  # 필요한 재료의 종류를 나타내는 변수
    stack = []  # 재료를 담는 스택
    ans = 0  # 조합의 수를 나타내는 변수

    for ingredient in ingredients:  # 주어진 재료 리스트를 순회하면서 처리
        if ingredient == need:  # 필요한 재료인 경우
            if stack and ingredient == 1 and stack[-1] == 3:
                # 스택이 비어있지 않고, 현재 재료가 1이며 스택의 마지막 재료가 3인 경우
                ans += 1  # 조합의 수를 증가시킴
                stack = stack[:-3]  # 스택에서 마지막 3개의 재료를 제거
                need = (need % 3) + 1  # 필요한 재료의 종류를 업데이트하고 1, 2, 3 순환
                continue  # 다음 재료로 넘어감

            need = (need % 3) + 1  # 필요한 재료의 종류를 업데이트하고 1, 2, 3 순환
            stack.append(ingredient)  # 현재 재료를 스택에 추가
        elif ingredient == 1:  # 현재 재료가 1인 경우
            stack = [ingredient]  # 스택을 1로 초기화
            need = 2  # 필요한 재료의 종류를 2로 설정
        else:  # 현재 재료가 1도 아니고 필요한 재료도 아닌 경우
            stack = []  # 스택을 초기화
            need = 1  # 필요한 재료의 종류를 1로 설정

    return ans  # 조합의 수 반환
