print('8)')
a,b=1,2
total=0
print(a,end=" ")
while a <= 4000000:
    if a% 2==0:
        total +=a
    print(a,end=" ")
    a,b=b,a+b
print("1nTong cac so chan trong day Finonacoi:", total)
