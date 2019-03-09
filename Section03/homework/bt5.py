sheeps = [5,7,300,90,24,50,75]
print("Hello my name is Truong and this is my ship flock")
print(sheeps)
big_sheep = max(sheeps)
posi_big = sheeps.index(big_sheep)
print("Now my biggest sheep has size 300 let's shear it")
sheeps[posi_big] = 8 
print(sheeps)

for i in range (1,3):
    sheeps = [x+50 for x in sheeps]
    print("Month:",i)
    print("One month has passed, now here is my flock",sheeps)
    print("Now my biggest sheep has size 350 lets shear it")
    sheeps[posi_big] = 8
    print("After shearing, here is my flock",sheeps)


print("My flock has size in total:",sum(sheeps))
print("I would get",sum(sheeps),"* 2$ =",sum(sheeps)*2,"$" )
