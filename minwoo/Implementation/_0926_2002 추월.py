# 들어오는대로 등수를 매기고 (해시)

# 나가는대로 등수를 매겨서 비교해본다

# 들어간 등수가 나올때 등수보다 적으면

# 추월한 차량임.

# 복잡도를 볼게 없다. 입력 데이터가 아주 적다.

n = int(input())

in_cars = {}
out_cars = {}

for i in range(n):
    car = input()
    in_cars[car] = i

for i in range(n):
    car = input()
    out_cars[car] = i

count = 0
out_keys = list(out_cars.keys())

for i in range(0, len(out_keys)-1):
    now_in = in_cars[out_keys[i]]
    for j in range(i+1, len(out_keys)):
        next_in = in_cars[out_keys[j]]
        if next_in < now_in:
            count += 1
            break

print(count)