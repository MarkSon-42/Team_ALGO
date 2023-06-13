# len  3 ~ 15

# - _ .

# . -> fornt != end !=     .. (<2)

# step 1 all lower()
# step 2 else delete
# step 3 .. -> .
# step 4 .'     '. -> delete
# step 5 isempty -> append('a')
# step 6 len 16 15
# step 7 a -> aaa   aa -> aaaaaa

# just sequencial implemetation (1 ~ 7)
def solution(new_id):
    rule_char = ['-', '_', '.']
    answer = ''
    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i] not in rule_char and not new_id.isalpha() and not new_id.isdigit():
            pass  # 조건식 수정해야 할듯 ???

        if new_id:
            pass
    return answer


# ..