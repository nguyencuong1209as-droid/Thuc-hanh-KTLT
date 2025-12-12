print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


lst = input("Nhập các từ: ").split()
maxlen = max(len(w) for w in lst)
for w in lst:
    if len(w) == maxlen:
        print(w)
