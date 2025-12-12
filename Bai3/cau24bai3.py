print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


s = input("Nhập câu: ")
upper = 0
lower = 0
for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
print("Chữ hoa:", upper)
print("Chữ thường:", lower)
