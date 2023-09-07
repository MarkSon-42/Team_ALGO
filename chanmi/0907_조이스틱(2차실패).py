def solution(name):
    # 'A' = 65
    # 'Z' = 90
    
    move_number = []
    answer_list = []
    visited = [False] * len(name)
    for letter in name:
        if letter <= "N":
            move_number.append(ord(letter) - 65)
        else:
            move_number.append(91 - ord(letter))
    
    print(move_number)

    def dfs(node, weight, count):
      # node = 현재 인덱스
      # weight = 상하 이동 횟수의 합
      # count = 현재 좌우 이동 횟수
      print(node)
      weight += move_number[node]
      print("현재 weight :", weight)
      print("현재 count :", count)
      move_number[node] = 0
      
      # 좌측 이동
      if node == len(name) * (-1):
        node_left = -1
      else:
        node_left = node - 1

      # 우측 이동
      if node == len(name) - 1:
        node_right = 0
      else:
        node_right = node + 1

      if not visited[node_left]:
        dfs(node_left, weight, count + 1)

      if not visited[node_right]:
        dfs(node_right, weight, count + 1)


    dfs(move_number, 0, 0, 0)
    print(answer_list)
    return answer_list[0]


    

solution("AKAAWAKX")