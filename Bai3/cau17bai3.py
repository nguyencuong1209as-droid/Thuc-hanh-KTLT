print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


n = int(input("Nhap n:"))
def sum_divisors(x):
    s = 0
    for i in range(1, x+1):
        if x % i == 0:
            s += i
    return s
for x in range(1, n):
    if sum_divisors(x) > x:
        print(x)
