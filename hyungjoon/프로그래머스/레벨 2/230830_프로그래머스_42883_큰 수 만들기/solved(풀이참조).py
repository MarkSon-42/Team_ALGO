'''
문제 : 큰 수 만들기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42883
소요 시간 : fail
'''
def solution(number, k):
    # 지워서 재배치하는게 아니라, 있는 순서대로 써야됨
    n = len(number)
    # 스택 활용하기
    stack = []
    
    # 스택의 마지막 값이 스택에 넣어야 하는 수보다 작다면, 크거나 같은 수가 나올때까지 pop해준다.
    for i in number:
        if not stack:
            stack.append(i)
            continue
        if k > 0:
            while stack[-1] < i:
                stack.pop()
                k -= 1
                # 스택이 비어버리거나 k만큼 뽑아냈을 때, break 한다.
                if not stack or k < 1:
                    break
        stack.append(i)
    
    # 10000, 2 일 경우, 제거 횟수를 다 사용하지 못함. 따라서 이를 앞에서부터 절삭해주는 작업
    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)

print(solution('4177252841', 4))