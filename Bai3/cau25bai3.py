print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


# Nhập dãy số từ người dùng (ví dụ: 1,2,3,4,5,6,7,8,9)
data = input("Nhập các số, cách nhau bởi dấu phẩy: ")
# Tách chuỗi thành danh sách số nguyên
numbers = [int(x) for x in data.split(",")]
# Lọc số lẻ
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Các số lẻ là:", odd_numbers)


