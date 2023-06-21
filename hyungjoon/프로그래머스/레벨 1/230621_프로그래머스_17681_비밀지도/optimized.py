def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        # bin을 쓰면 0b가 앞에 붙어서 2번 인덱스부터 출력
        # bin(i|j) 는 i와 j를 2진법으로 바꿔서 비트연산된 값을 반환한다.
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28])