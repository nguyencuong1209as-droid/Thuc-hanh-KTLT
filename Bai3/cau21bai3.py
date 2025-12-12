print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


s = input("Nhập chuỗi số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")
lst = s.split(",")
result = []
for x in lst:
    if int(x, 2) % 5 == 0:   
        result.append(x)
print(",".join(result))
