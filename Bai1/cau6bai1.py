print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


nums=[]
for i in range (2000,3201):
    if i% 7==0 and i%5!=0:
        nums.append(str(i))
print(",".join(nums))

