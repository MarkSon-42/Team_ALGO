# 예외처리 : PS에서..
# 에러 발생해도 프로그램 죽지 않게
# https://blockdmask.tistory.com/537
print("== ProgramStart")

try:
    a = 99 / 0  # division zero
    print(f"99/0 : {a}")  # error 발생시 바로 except로 넘어간다.
    # 따라서 위 프린트문은 실행조차 안됨.
except:
    print("error! change division number : not 0")

finally:
    print("에러가 발생해도 안해도 무조건 거치는 문구가 finally")

print("== ProgramEnd")

#