
items = ["T-shirt","Sweater"]
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if n == "R":
        print("Our items:",items)
    elif n =="C":
        new_i = input("Enter your item:")
        items.append(new_i)
        print("Our item:",items)
    elif n == "U":
        update_posi = int(input("Update position ?"))    
        if update_posi <= len(items): 
            new_i = input("New item ?")
            items.insert(update_posi,new_i)
            print("Our items:", items)
        else:
            print("Your position does not exist, please try again !")
            update_posi = int(input("Update position?"))
            new_i = input("New item ?")
            items.insert(update_posi,new_i)
            print("Our items:", items)
    if n == "D":
        Del_posi = int(input("Delete position?"))
        items.remove("del_posi")
        print("Our items:", items)
    break