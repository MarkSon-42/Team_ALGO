# 첫 풀이 시간 : 40min

import sys
input = sys.stdin.readline

def find_move_num_left(name):
    cnt = 0
    last_idx = name_len - 1
    if name[last_idx] == 'A':
        while name[last_idx] == 'A':
            last_idx -= 1
    new_name = name[:last_idx + 1]
    name_new_len = len(new_name)

    first_idx = 0
    while (first_idx <= last_idx):
        cnt += 1
        if new_name[first_idx] != 'A':
            if new_name[first_idx] <= 'M':
                cnt += new_name[first_idx] - 'A'
            else:
                cnt += 'Z' - new_name[first_idx] + 1
        first_idx += 1

    return cnt

def find_move_num_right(name):
    cnt = 0
    first_idx = 0
    if name[first_idx] == 'A':
        while name[first_idx] == 'A':
            first_idx += 1
    new_name = name[first_idx:]
    name_new_len = len(new_name)

    last_idx = name_len - 1
    while (first_idx <= last_idx):
        cnt += 1
        if new_name[last_idx] != 'A':
            if new_name[last_idx] <= 'M':
                cnt += new_name[last_idx] - 'A'
            else:
                cnt += 'Z' - new_name[first_idx] + 1
        last_idx -= 1

    return cnt + 1

def find_move_num_right(name):
    answer = 0
    return answer

name = list(input().split())
name_len = len(name)

left_num = find_move_num_left(name)
right_num = find_move_num_right(name)

min_num = left_num if left_num < right_num else right_num
print(min_num)
