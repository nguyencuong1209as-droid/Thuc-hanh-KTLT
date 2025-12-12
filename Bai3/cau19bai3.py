print(" Sinh vien : Nguyen Van Cuong")
print(" Ma so SV: 245751030110048")
print("##############################")


limit = 1_000_000
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if prime[i]:
        for j in range(i*i, limit, i):
            prime[j] = False
P = tuple(i for i in range(limit) if prime[i])
print("Tuple P da tao xong,so luong so nguyen to:", len(P))
