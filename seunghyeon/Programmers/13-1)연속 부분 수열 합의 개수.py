def solution(elements):
	rst = set()

	elements = elements * 2
	elementLen = len(elements)

	for i in range(elementLen):
		for j in range(elementLen):
			rst.add(sum(elements[j : j + i + 1]))
	
return(len(rst))
