### 아래 방식으로 했을 때 시간초과 발생

# def solution(n, left, right):
#     answer = []
#     for i in range(n):
#         answer.append([])
        
#         k = i + 1
#         for j in range(n):
#             if j <= i:
#                 answer[i].append(k)
#             else:
#                 k += 1
#                 answer[i].append(k)
#     # print(answer)
#     final_answer = []
#     for row in answer:
#         final_answer.extend(row)
    
#     return final_answer[left:right + 1]


# 위 코드를 챗GPT가 최적화 해준 코드

def solution(n, left, right):
    answer = []

    # 행과 열의 차이에 따라 패턴을 생성하여 answer에 추가
    for i in range(left, right + 1):
        row = i // n  # 행 번호 계산
        col = i % n  # 열 번호 계산
        value = max(row, col) + 1  # 패턴 값 계산
        answer.append(value)

    return answer
