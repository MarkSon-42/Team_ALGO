def solution(name):
    change_alpha_num = [min(abs(ord('A')-ord(c)), 26-abs(ord('A')-ord(c))) for c in name]

    min_move = len(name) - 1
    for i, c in enumerate(name):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)
    
    return sum(change_alpha_num) + min_move