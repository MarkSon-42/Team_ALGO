import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input())
	words = []
	for _ in range(N):
		words.append(my_input())

	shortcut = set([' '])
	splited = []
	for w in words:
		temp = w.split()
		haveShortcut = False
		for i in range(len(temp)):
			if temp[i][0].upper() not in shortcut:
				shortcut.add(temp[i][0].upper())
				temp[i] = '[' + temp[i][0] + ']' + temp[i][1:]
				splited.append(" ".join(temp))
				haveShortcut = True
				break
		if not haveShortcut:
			for i in range(len(w)):
				if w[i].upper() not in shortcut:
					shortcut.add(w[i].upper())
					splited.append(w[:i] + '[' + w[i] + ']' + w[i+1:])
					haveShortcut = True
					break
		if not haveShortcut:
			splited.append(" ".join(temp))
	for s in splited:
		print(s)
