print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


def benefit(t, n, k):
    if t < 0 or n < 0 or k < 0:
        print("Tham số không hợp lệ!")
        return
    final_money = n * ((1 + t/100) ** k)
    return final_money
t = float(input("Nhập lãi suất theo %/tháng: "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))
result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", result)
