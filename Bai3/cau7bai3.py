print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


s = input("Nhap chuoi:")
new_s = ""
for ch in s:
    if not ch.isdigit():
        new_s += ch
print("Chuoi sau khi bo chu so:", new_s)
