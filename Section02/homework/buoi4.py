# n = int(input("Nhap nam sinh cua mot nguoi:"))
# age = 2019 - n
# if age < 10:
#     print("Baby")
# elif (10<age<16):
#     print("teen")
# else: print("Adult")

# yob = (input("Nhap nham sinh:"))
# while not yob.isdigit():
#     print("Nhap sai roi,dmm")
#     yob = input("Nhap nam sinh")
# age = 2019 - int(yob)
# print("tuoi cua ban la:",age)

# while False:
#     print("hi")

# password = input("Moi nhap password:")

# while True:
#     if len(password)>8:
#         break
#     print("Moi nhap lai pass")
#     password = input("Moi ban nhap lai password")

# print("password ban vua nhap la",password)


# loop_count = 0
# while True:
#     print("loop count:", loop_count)
#     loop_count = loop_count+1
#     if loop_count>=3:
#         break
# print("Da chay xong")

#GIẢI PHƯƠNG TRÌNH BẬC 2
# a = input("Nhap he so a:")
# while not a.isdigit():
#     print("Xin moi nhap so")
#     a = input("Nhap he so a:")
# b = input("Nhap he so b:")
# while not b.isdigit():
#     print("Xin moi nhap so")
#     b = input("Nhap he so b:")
# c = (input("Nhap he so c:"))
# while not c.isdigit():
#     print("Xin moi nhap so")
#     c = input("Nhap he so c:")

# a = int(a)
# b = int(b)
# c = int(c)

# delta = b**2-(4*a*c)
# if delta < 0:
#     print("Phuong trinh vo nghiem")
# if delta == 0:
#     x = -(b/2*a)
#     print("Phuong trinh co nghiem duy nhat:",x)
# if delta > 0:
#     x1 = (- b + (delta**0.5)) / (2*a)
#     x2 = (- b - (delta**0.5)) / (2*a)
#     print("Phuong trinh co 2 nghiem phan biet la:",)
#     print("x1=",x1)
#     print("x2=",x2)

ls=[]
n = int(input("Nhap vai n so nguyen:"))
for i in range(n):
    print("Nhap phan tu thu:",i)
    so=int(input(""))
    ls.append(so)
print("Day vua nhap la:")
print("ls:")

print("Tong day vua nhap:")
print(sum(ls))
print("Phan tu thu 2 trong day")
print(ls[1])

