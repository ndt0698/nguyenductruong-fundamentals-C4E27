print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x+3) ?")
answer = {
    "1.":"35",
    "2.":"36",
    "3.":"40",
    "4.":"44"
}
for i in answer:
    print(i,answer[i])
n = int(input("Your choice:"))
if n == 4:
    print("Correct !")
else:
    print("Wrong !")