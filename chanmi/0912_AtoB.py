import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A, B = map(int, input().split())

count = 0
is_made = False

while A < B:
  if B % 2 == 0:
      # B가 짝수인 경우
      B = B // 2
      count += 1

  elif B % 10 == 1:
     # 1로 끝나는 경우
     B = B // 10

     count += 1
  else:
     break
  
  if A == B:
     count += 1
     is_made = True
     break
  
if is_made == True:
   print(count)
else:
   print(-1)