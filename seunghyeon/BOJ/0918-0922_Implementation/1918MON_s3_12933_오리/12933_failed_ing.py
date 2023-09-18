import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	record = my_input().rstrip()

	len_record = len(record)
	quack, quack_idx = list('quack'), [0]
	ducks, ducks_last_idx = [[]], 0
	for c in range(len_record):
		if c == 0:
			if record[c] == 'q':
				ducks[0].append('q')
				ducks_last_idx += 1
				quack_idx[0] += 1
			else:
				print(-1)
				sys.exit()
		else:
			# q가 새로 시작될 경우
			if record[c] == 'q':
				same_duck = 0
				for duck in ducks:
					if duck[-1] == 'k':
						duck.append(quack[quack_idx[ducks.index(duck)] % 6])
						quack_idx[ducks.index(duck)] += 1
						same_duck = 1
						break
				if same_duck == 0:
					ducks.append(['q'])
					quack_idx.append(1)
					ducks_last_idx += 1
			else:
				duck_exit = 0
				for duck in ducks:
					if duck[-1] == quack[(quack_idx[ducks.index(duck)] - 1) % 6 if quack_idx[ducks.index(duck)] % 6 != 0 else 5]:
						duck.append(quack[quack_idx[ducks.index(duck)] % 6])
						quack_idx[ducks.index(duck)] += 1
						duck_exit = 1
						break
				if duck_exit == 0:
					print(-1)
					sys.exit()

	for duck in ducks:
		if len(duck) % 5 != 0:
			print(-1)
			sys.exit()

	print(len(ducks))


# ducks_last_idx가 필요할까? 필요없으면 지우기

