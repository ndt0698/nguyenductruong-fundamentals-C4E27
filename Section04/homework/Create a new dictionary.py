prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
for a in prices:
    print(a)
    print("prices:",prices[a])
    print("stock:", stock[a])
    print("")
    b = int(prices[a]*stock[a])
    total = total + b 
    
print("total:",total)
    