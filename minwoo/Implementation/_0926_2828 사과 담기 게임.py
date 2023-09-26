n, m = map(int, input().split())
j = int(input())

move = 0
bucket_right = m
bucket_left = 1

for _ in range(j):
    apple = int(input())

    if bucket_left <= apple <= bucket_right:
        continue
    if apple < bucket_left:
        move += (bucket_left - apple)
        bucket_right -= (bucket_left - apple)
        bucket_left = apple
    else:
        move += (apple - bucket_right)
        bucket_left += (apple - bucket_right)
        bucket_right = apple

print(move)


