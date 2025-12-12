print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


balance = 0
print("Nhập nhật ký giao dịch (D/W). Nhập dòng trống để kết thúc.")
while True:
    line = input()
    if not line: 
        break
    action, amount = line.split()
    amount = int(amount)
    if action.upper() == "D":
        balance += amount
    elif action.upper() == "W":
        balance -= amount
print("Số dư cuối cùng là:", balance)
