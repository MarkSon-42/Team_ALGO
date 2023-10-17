import sys
my_input = sys.stdin.readline


def execute_inst(problem_dic, instruction_lst):
	for inst in instruction_lst:
		if inst[0] == "add":
			problem_dic[inst[1]] = inst[2]
		elif inst[0] == "solved":
			del problem_dic[inst[1]]
		else:
			if inst[1] == 1:
				max_level = max(problem_dic.values())
				max_lev_problems = [key for key, val in problem_dic.items() if max_level == val]
				print(max(max_lev_problems))
			else:
				min_level = min(problem_dic.values())
				min_lev_problems = [key for key, val in problem_dic.items() if min_level == val]
				print(min(min_lev_problems))


N = int(my_input())  # 문제의 개수
problems = {}
for _ in range(N):
	k, v = map(int, my_input().split())
	problems[k] = v
M = int(my_input())  # 명령의 개수
instructions = []
for _ in range(M):
	instruction = my_input().split()
	if instruction[0] == 'add':
		instruction[1] = int(instruction[1])
		instruction[2] = int(instruction[2])
	else:
		instruction[1] = int(instruction[1])
	instructions.append(instruction)

execute_inst(problems, instructions)