# n = int(input("Nhap n so tu ban phim:"))
# tong = 0
# for i in range(n):
#     so = int(input("Nhap so"))
#     tong = tong + so
# print(tong)


# m = int(input("Nhap m so tu ban phim:"))
# tongg = 0 
# for i in range(m):
#     num = int(input("Nhap so:"))
#     tongg = (tongg + num )
# tbc = tongg / m
# print(tbc)


# def add_two_number(a,b):
#    return a+b

# num1 = int(input("Số thứ nhất:"))
# num2 = int(input("Số thứ hai :"))
# num3 = int(input("Số thứ hai :"))

# sum_1_2= add_two_number(num1,num2)
# sum_3 = add_two_number(sum_1_2,num3)
# print("tong ba so la:",sum_3)


# def abs_of_number(a):
#     if a > 0:
#         return a
#         print("Tri tuyệt đối là:",a)
#     else:
#         return -a
#         print("Tri tuyet doi la:",-a)
#     print("Tri tuyet doi la:",a)

# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)
# print(x)
# print(tong)


# def eveluate(a,b,operator):
#     if  operator=="*":
#         return a*b
#     elif operator=="+":
#         return a+b
#     elif operator=="-":
#         return a-b
#     elif operator=="/":
#         return a/b
#     else:
#         return None
    
# x = eveluate(10,5,"*")
# print(x)



def check_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i ==0:   
            return False
    return True

so = int(input("So can kiem tra:"))
for v in range(2,so+1):
    if check_prime(v):
        print("so nguyen to la:",v)

    
