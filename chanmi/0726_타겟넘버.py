def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    return answer

# DFS랑 BFS 공부를 더 하긴 해야할듯...
def dfs(numbers, target, index, current):
    global answer
    
    # 마지막에 다다른 경우
    if index == len(numbers):
        if current == target:
            answer += 1
        return
    
    dfs(numbers, target, index + 1, current + numbers[index])
    dfs(numbers, target, index + 1, current - numbers[index])