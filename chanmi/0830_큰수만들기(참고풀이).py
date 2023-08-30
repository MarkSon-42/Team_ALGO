def solution(number, k):

    # itertools의 combination의 시간복잡도를 줄일 방법을 찾다가
    # chatGPT에게 물어보니 stack을 활용하는 방법을 알려줌...
    
    stack = []
    
    for num in number:
        # 스택의 가장 나중에 넣은 숫자보다 큰 숫자면 앞에 있는 걸 빼고 숫자를 넣는 방식
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
            
        stack.append(num)
    
    # 987654321 같이 위에 있는 while문을 돌지 않을 경우, 뒤에서부터 지워줌
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)