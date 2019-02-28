#Điều kiện lồng là trong một câu lệnh if, chúng ta có thêm các cậu lệnh if và else khác trong đó. 
a = int(input("Nhập vào a:"))
b = int(input("Nhập vào b:"))



if a > b :
    print("a lớn hơn b")
else:
    if a < b:
        print("a nhỏ hơn b")
    elif a == b:
        print("a bằng b")    
    

