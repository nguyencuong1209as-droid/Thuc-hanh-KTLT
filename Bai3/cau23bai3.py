print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


s = input("Nhập câu: ")
letters = 0
digits = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
print("Số chữ cái là:", letters)
print("Số chữ số là:", digits)
