import random
word = ["lovely","bullshit","holyfucker","comdom","asshole","shutthefuckup"]

Quiz_1 = random.choice(word)
suft = list(Quiz_1)
random.shuffle(suft)
check = Quiz_1
for i in range(len(suft)):
    print(suft[i],end=" ")
n = input("Your answer:")

while True:
    if n == check:
        print("Nó lại là đúng vãu l**")
        break
    else:
        print("Bạn sai rồi !")
        print("Nhập con mẹ mày lại đi:")
        n = input("Your answer:")
        


