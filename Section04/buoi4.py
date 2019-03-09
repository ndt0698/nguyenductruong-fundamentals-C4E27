# Nhập n số từ àn phím 
# in ra dãy vừa Nhập
# tìm các cặp số trong dãy có tổng là một số chẵn 


# n = 4
# m = 4
# ds=[3,8,7,4]
# for i in range(m):
#     for j in range(i+1,n):
#         print("i=",i,"j=",j,"cap la:",ds[i],ds[j])
#         if (ds[i] + ds[j])% 2 == 0:
#             print("cac cap so can tim la:", ds[i],ds[j])



#Tìm các bộ 3 số x,y,z sao cho :
#0<=x,y,z<=100
#x bình + y bình + z bình = x.y.z

# n=100
# for x in range(1,n):
#     for y in range(1,n):
#         for z in range(1,n):
#             if x**2 + y**2 + z**2 == x*y*z:
#                 print("Bộ 3 số cần tìm là:",x,y,z)

# person={"name":"Nguyen van A","Age":12}
# if 'address' in person:
#     addr=person["address"]
#     print(addr)

#Bài toán từ điển
# tudien = {"computer":"Máy tính","mouse":"Con chuột","keyboard":"Bàn phím"}
# print(tudien)
# while True:
#     n = input("Xin mời nhập vào một từ bất kỳ:")
#     if n in ['quit','exit']:
#         break
#     if n in tudien:
#         print(tudien[n])
#     else:
#         m = input("ý nghĩa của từ này là gì ?, Xin mời bạn thêm nghĩa: ")
#         tudien[n]=m
#         print(tudien[n])

# duyệt theo key xem trong từ điển có những từ gì
# for v in tudien:
#     print(v)

#duyệt theo value 
#for v in tudien.values:
#   print(v)


tap_nguoi=[]
nguoi_1={
    "name":"Nguyen van A",
    "age":12,
    "add":"Hanoi",
    "sdt":["0123","43434"]
}
tap_nguoi.append(nguoi_1)
print(tap_nguoi[0]["sdt"][1])



