# -------------------- < Multi Set > --------------------

# 1. 다중 집합이란?
    # 기존에 파이썬에서 집합은 보통 set으로 사용
    # set은 중복된 원소를 허용하지 않음
    # So, 중복된 원소를 포함하는 개념인 다중집합 표현을 위해서는 list를 사용
    # 즉 개념만 다중집합, 실체는 list


# .
# .
# .


# 2. ///code/// 다중 집합의 합집합 a_rst
a = [1, 2, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4, 6]

a_tmp = a.copy()
a_rst = a.copy()

for i in b:
    if i not in a_tmp:
        a_rst.append(i)
    else:
        a_tmp.remove(i)
print(a_rst)
    ## [1, 2, 2, 3, 4, 5, 1, 6]


# .
# .
# .


# 3. ///code/// 다중 집합의 교집합 a_rst
a = [1, 2, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4, 6]

rst = []
for i in b:
    if i in a:
        a.remove(i)
        rst.append(i)
print(rst)
    ## [1, 2, 3, 4]
