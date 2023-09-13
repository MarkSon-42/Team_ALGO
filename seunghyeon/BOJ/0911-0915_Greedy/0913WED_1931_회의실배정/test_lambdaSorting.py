lst = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
lst1 = sorted(lst, key=lambda x: (x[1], x[0]))
lst2 = sorted(lst, key=lambda x: (x[0], x[1]))
print(lst1)
print(lst2)

lst3 = sorted(lst, key=lambda x: x[1])
lst3 = sorted(lst3, key=lambda x: x[0])
print(lst3)

lst4 = sorted(lst, key=lambda x: x[0])
print(lst4)
lst4 = sorted(lst4, key=lambda x: x[1])
print(lst4)


# 결론:
	# 키에 하나씩만 적을때에는, 궁극적으로 원하는거 (젤 중요한거)를 마지막에 sorting하고
	# 한 번에 두 개 적을 때에는 하나씩적을 때의 순서 반대로 적으면 됨