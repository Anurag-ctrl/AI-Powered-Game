import random
import time
cs=0
ps=0
list = ['1','2']
#Take main input
while True:
    a=input("Enter a number\n")
    #If the input goes wrong then demand a correct one in contini...
    while a not in list:
        print('Invalid Entry !')
        a = input("Enter a number\n")
    a=int(a)
    #Real game begins and the score start calculated
    if a == random.randint(1,2):
        cs=cs+1
        print("Player Score =",ps,"\n","Computer Score =",cs)
    else:
        ps +=1
        print("Player Score =", ps, "\n", "Computer Score =", cs)
    #If either the score has reached the half point that is 5 then half-time will start
    #practically two half time will be there in our game. of each 60 sec(1min)
    if ps==5:
        print('Half Time')
        time.sleep(55)
        print('Game About to Begin')
        for t in range(5,0,-1):
            time.sleep(1)
            print('Game Starting in',t,'Seconds..')
    elif cs==5:
        print('Half Time')
        time.sleep(60)
        print('Game About to Begin')
        for t in range(5, 0, -1):
            time.sleep(1)
            print('Game Starting in', t, 'Seconds..')
    #Final Results
    if ps==10:
        print('Player Won')
        break
    elif cs==10:
        print('Computer Won')
        break
