print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x+3) ?")
answer = {
    "1.":"35",
    "2.":"36",
    "3.":"40",
    "4.":"44"
}
total = 0
for i in answer:
    print(i,answer[i])
n = int(input("Your choice:"))
if n == 4:
    print("Correct !")
    total = total + 1
else:
    print("Wrong !")

print("Jack scored these marks in math tests: 49, 81, 72, 66 and 52. What is the mean ? ")
math = {
    "1.":"About 55",
    "2.":"About 65",
    "3.":"About 75",
    "4.":"About 85"
}
for j in math:
    print(j,math[j])
m = int(input("Your choice:"))
if m == 2:
    print("Correct !")
    total = total + 1
else:
    print("Wrong !")

if total == 2:
    print("Your correctly answer 2 out of 2 questions ")
if total == 1:
    print("Your correctly answer 1 out of 2 questions ")
if total == 0:
    print("Your correctly answer 0 out of 2 questions ")

