# 16:30
import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input().rstrip())
	alpha_v = [0 for _ in range(26)]

	ops, lower_ops, words = [], [], []
	for _ in range(N):
		op = input().rstrip()
		ops.append(op.split())
		lower_ops.append((op.lower().split()))
		words = list(set(sum(lower_ops, [])))
	dict_words_v = dict.fromkeys(words, 0)  # #####

	for op in lower_ops:
		target_word_idx = -1
		target_c_idx = -1
		for word in op:
			if dict_words_v[word] == 0:
				dict_words_v[word] = 1
				target_word_idx = op.index(word)
				break
		if target_word_idx == -1:
			for word in op:
				for c in word:
					if alpha_v[ord(c)-ord('a')] == 0:
						alpha_v[ord(c) - ord('a')] = 1
						target_c_idx = word.index(c)
		origin_op = ops[lower_ops.index(op)]
		rst_lst = []
		rst_lst.append(' '.join(origin_op[:target_word_idx]))
		tmp1, tmp2 = origin_op[target_word_idx].split(origin_op[target_word_idx][target_c_idx])
		rst_lst.append(tmp1+'['+origin_op[target_word_idx][target_c_idx]+']'+tmp2)
		rst_lst.append(' '.join(origin_op[target_word_idx+1:]))

		print(''.join(rst_lst))




# defaultdict 사용하는 방법도 있다고 함