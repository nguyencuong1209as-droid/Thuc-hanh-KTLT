print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


n = int(input("Nhập n: "))
fib = [0, 1]
while fib[-1] + fib[-2] < n:
    fib.append(fib[-1] + fib[-2])
print("Cac so Fibonacci nho hon n:")
print(fib)
