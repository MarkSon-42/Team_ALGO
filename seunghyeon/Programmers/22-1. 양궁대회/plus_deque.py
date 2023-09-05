# deque에 대해 알아보고 간단히 실습해보았다.




from collections import deque

# 1. 초기화 관련 ----------------------------------------------
# 비어있는 새 큐 만들기
Deque = deque()

# 원소가 들어있는 큐 만들기
Deque = deque([1, 2, 3])

# 큐 최대 길이 명시하기
    # 원소를 maxlen보다 더 많이 넣으면 maxlen 자동 갱신
Deque = deque(maxlen = 100)



# 2. append 관련 ---------------------------------------------
Deque.append(3)
Deque.append(6)
Deque.append(9)
print(Deque) ## Deque([3, 6, 9], maxlen = 100)

Deque.appendleft(3)
Deque.appendleft(6)
Deque.appendleft(9)
print(Deque) ## Deque([9, 6, 3, 3, 6, 9], maxlen = 100)



# 3. pop 관련 ------------------------------------------------
for i in range(3):
    print(Deque.popleft())
## 9
## 6
## 3

for i in range(3):
    print(Deque.pop())
## 9
## 6
## 3



# 4. extend 관련 ---------------------------------------------
Deque.extend('d')
Deque.extend('e')
Deque.extend('f')
print(Deque)
## deque(['d', 'e', 'f'], maxlen=100)

Deque.extendleft('c')
Deque.extendleft('b')
Deque.extendleft('a')
Deque.extendleft('msh')
print(Deque)
## deque(['h', 's', 'm', 'a', 'b', 'c', 'd', 'e', 'f'], maxlen=100)



# 5. insert, remove 관련 -------------------------------------
Deque.remove('s')
Deque.remove('h')
Deque.remove('m')
print(Deque)
## deque(['a', 'b', 'c', 'd', 'e', 'f'], maxlen=100)
    # 만약 같은 항목이 있었다면, 왼쪽에 있는 것부터 삭제

Deque.insert(0, 'A')
print(Deque)
## deque(['A', 'a', 'b', 'c', 'd', 'e', 'f'], maxlen=100)

Deque.insert(1, 'LOVE') 
print(Deque)
## deque(['A', 'LOVE', 'a', 'b', 'c', 'd', 'e', 'f'], maxlen=100)



# 6. rotate 관련 ---------------------------------------------
newTest = [1, 2, 3, 4, 5, 6, 7, 8, 9]
testDeque = deque(newTest)
print(testDeque)
## deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

testDeque.rotate(3)
print(testDeque)
## deque([7, 8, 9, 1, 2, 3, 4, 5, 6])

testDeque.rotate(-3)
print(testDeque)
## deque([1, 2, 3, 4, 5, 6, 7, 8, 9])



# 7. clear 관련 ----------------------------------------------
testDeque.clear()
print(testDeque)
## deque([])
