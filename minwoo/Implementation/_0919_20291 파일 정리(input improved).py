import sys
input = sys.stdin.readline
n = int(input())

extension_name = []

for _ in range(n):
    file_name = input().strip()  # readline의 줄바꿈 포함을 여기서 처리해준다
    for j in range(len(file_name)-1, -1, -1):
        if file_name[j] == '.':
            extension_name.append(file_name[j+1:])
extension_name.sort()
cnt = {}

for name in extension_name:
    if name in cnt:
        cnt[name] += 1
    else:
        cnt[name] = 1

for name, freq in cnt.items():
    print(f"{name} {freq}")


# ????
# import sys
# input = sys.stdin.readline으로 input()을 받으면 출력이 이상하게 된다
# icpc
# 2
# spc
# 2
#..... print에 end조건을 넣어도 그럼. sys.stdin.readline을 공부해야..


# chatGPT

# readline() 메서드: sys.stdin 객체에는 readline() 메서드가 있습니다.
# 이 메서드는 표준 입력에서 한 줄씩 읽어옵니다. 줄바꿈 문자('\n')를 만날 때까지
# 문자를 읽어오고, 줄바꿈 문자를 포함하여 반환합니다
# readline()은 반환값에 '\n'이 들어있음.
# strip을 해주면 해결가능.