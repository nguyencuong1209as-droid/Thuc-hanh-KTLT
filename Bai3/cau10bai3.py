print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


ds=input('Nhap chuoi: ').split()
if len (ds) >= 2:
    new_ds = ds[1:-1]
else:
    new_ds = []
print("List sau khi bo phan tu dau va cuoi:",new_ds)
