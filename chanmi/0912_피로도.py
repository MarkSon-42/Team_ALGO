import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

# 한 시간 일하면 피로도는 A만큼 쌓임
# 한 시간 일하면 B만큼 일할 수 있음
# 한 시간 쉬면 C만큼 줄어들음
# 피로도는 M을 넘지 않게

if A > M:
    print(0)

else:
  current_fatigue = 0
  current_work = 0
  hour = 24

  while hour:
      # 일할 수 있는 경우
      if current_fatigue + A <= M:
          current_fatigue += A
          hour -= 1
          current_work += B
      # 쉬어야 하는 경우
      else:
          current_fatigue -= C
          if current_fatigue < 0:
              current_fatigue = 0
          hour -= 1

  print(current_work)