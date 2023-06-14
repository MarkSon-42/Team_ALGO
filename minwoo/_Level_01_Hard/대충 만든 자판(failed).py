def solution(keymap, targets):
    answer = []
    cnt = 0
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] == targets[i][j]:
                cnt += 1
                break
            else:
                continue
    return answer

# ... ???? 