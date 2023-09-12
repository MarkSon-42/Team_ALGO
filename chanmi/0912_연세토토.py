import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

sub_num, mile = map(int, input().split())

class_info = [0] * sub_num

for i in range(sub_num):
    P, L = map(int, input().split())
    if P < L:
        # 아직 수강 가능한 경우:
        mile_list = list(map(int, input().split()))
        class_info[i] = 0
        continue
    else:
      mile_list = list(map(int, input().split()))
      mile_list.sort()
      class_info[i] = mile_list[P - L]



# 투자 가능한 마일리지는 1에서 36까지
# class_info에서 0인 값은 1점만 넣어도 들을 수 있는 과목이므로
# 최대한 많이 들어야 하니 0의 개수만큼 1점 사용

class_info.sort()
subject_num = 0

for i in range(sub_num):
  if class_info[i] == 0 and mile - 1 >= 0:
    subject_num += 1
    mile -= 1
    continue
  elif class_info[i] == 0 and mile - 1 < 0:
     break

  if mile - class_info[i] >= 0:
    subject_num += 1
    mile -= class_info[i]
  else:
    break
   
print(subject_num)