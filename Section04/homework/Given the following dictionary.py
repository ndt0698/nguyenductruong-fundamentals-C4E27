
inven = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']}

inven["pocket"] = ["seashell","strangeberry","lint"]
inven["backpack"].remove("dagger")
inven["gold"] += 50
print(inven)

