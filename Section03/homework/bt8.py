#a\20 x 1 stars:
# for a in range(20*1):
#     print("*",end="")


#b\n stars (n is entered by users)
# n = int(input("Enter a number:"))
# for b in range(n):
#     print("*",end="")


#c\9 stars and xs in total
# for c in range(4):
#     print("x",end=' * ')
# print("x")


#d\ n stars and xs in total (n is entered by users)
# n = int(input("Enter a number:"))
# if n%2==0:
#     for a in range(int(n/2)):
#         print("x",end=' * ')
# else:
#     for i in range(int((n-1)/2)):
#         print("x",end=' * ')
#     print("x")


#f\7 x 3 stars
# for a in range(3):
#     for b in range(7):
#         print("*",end=' ')
#     print()

#g\ n x m stars (n, m are entered by users)
n = int(input("Enter n: "))
m = int(input("Enter m: "))
for a in range(m):
    for b in range(n):
        print("*",end=' ')
    print()
    

