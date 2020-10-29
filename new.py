import random
cs=0
ps=0
list = [1,2]
a=input("Enter a number\n")
while True:
    if a not in list:
        input("Enter a number\n")
    else:
        break
if a == random.randint(1,2):
    cs=cs+1
    print("Player Score =",ps,"\n","Computer Score =",cs)
else:
    ps +=1
    print("Player Score =", ps, "\n", "Computer Score =", cs)
