N = int(input())
stairs = [0]
dp_table = [0] * (N+1)

for j in range(1,N+1):
    stairs.append(int(input()))
    if j == 1 :
        dp_table[1] = stairs[1]
    elif j == 2 :
        dp_table[2] = stairs[1] + stairs[2]
    else:
        dp_table[j] = max(stairs[j] + stairs[j-1] + dp_table[j-3], stairs[j] + dp_table[j-2])

print(dp_table[N])

#제일 조심해야 할 조건은 연속된 3칸을 밟으면 안되기 때문에 트리 형태로 한 칸밟을때의 경우, 두 칸 밟을 때의 경우 ... 도착까지 그려 봤더니, \
# 일단 1칸더 올라가거나, 2칸 올라갈때를 나눠야 하고, 연속 3칸 경우를 방지 하기 위해 한 칸 : stairs[j] + stairs[j-1] + dp_table[j-3], 
# 두 칸 : stairs[j] + dp_table[j-2] 이렇게 경우를 나눠 주었다. 그래서 dp table에 각 경우의 점수를 더한 결과를 저장하고 max로 큰 값만 
# 저장 될 수 있도록 하였다. 마지막 도착지에서의 dp table에 누적된 칸의 점수 합을 반환하였다.
