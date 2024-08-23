import random
'''
1 for rock
-1 for paper
0 for scissor

two main i/o: computer  and user

'''

computer = random.choice([-1, 0, 1])

userstr = input("enter your choice : ")
youDict = {"r":1,"p":-1,"s":0}

reverseDict ={1:"rock",-1:"paper",0:"scissor"}

user = youDict[userstr]


print(f"you choose {reverseDict[user]} \ncomputer choose {reverseDict[computer]}")

if(computer==user):
    print("match draw")
else :
    if(computer == 1 and user == 0):
        print("You loose !:-(")
    elif(computer == 1 and user == -1):
        print("You Win !(⌐■_■)")
    elif(computer == -1 and user == 0):
        print("You Win !(⌐■_■)")
    elif(computer == -1 and user == 1):
        print("You loose !:-(")
    elif(computer == 0 and user == 1):
        print("You loose !:-(")
    elif(computer == 0 and user == -1):
        print("You Win !(⌐■_■)")
    else:
        print("something went wrong")



