# set을 활용해 중복을 제거해주고
# 쿠폰번호가 없다면 추가해준 후,
# set의 길이와 정답변수를 비교해 최댓값으로 저장해주고
# 포인터를 1씩 늘림

# https://velog.io/@highero-k/%EB%B0%B1%EC%A4%80-2531-%ED%9A%8C%EC%A0%84-%EC%B4%88%EB%B0%A5-Python-%EC%8B%A4%EB%B2%84-1


import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
  sushi.append(int(input()))

left, right = 0, k
answer = 0
while left < n:
  s = set()
  for i in range(left, right):
    s.add(sushi[i%n])
  if c not in s:
    s.add(c)

  answer = max(answer, len(s))
  left += 1
  right += 1

print(answer)

# 아직 이해 못한 풀이.. 설명이 없음.