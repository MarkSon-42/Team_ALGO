t = int(input())

for _ in range(t):
    b1, b2 = map(str, input().split())
    c = int(b1, 2) + int(b2, 2)
    print(bin(c)[2:])



############ method : int(value, base)############

# print(int())
# print(int('11'), 2)
# print(int('1a', 16))
# print(int('11001', 2))
