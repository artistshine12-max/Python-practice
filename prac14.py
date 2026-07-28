#Snake, water and gun game using python:
#using random computer's choice will be auto-generated randomly out of available three choices:
import random
comp=["snake", "water", "gun"]
computer = random.choice(comp)
#input user's choice:
youstr= input("Enter your choice: ")
youDict ={ "s":"snake", "w": "water", "g": "gun"}
you= youDict[youstr]
#comparing the user's choice and computer's choice and generating the result:
if(computer =="water" and you=="snake"):
    print("You won!")
elif(computer =="water" and you=="gun"):
    print("You lost and Computer won!")
elif(computer =="water" and you=="water"):
    print("Match drew!")
elif(computer =="snake" and you=="gun"):
    print("You won!")
elif(computer =="snake" and you=="water"):
    print("You lost and Computer won!")
elif(computer =="snake" and you=="snake"):
    print("Match drew!")
elif(computer =="gun" and you=="gun"):
    print("Match drew!")
elif(computer =="gun" and you=="snake"):
    print("You lost and Computer won!")
elif(computer =="gun" and you=="water"):
        print("You won!")
else:
    print("Match drew!")    

    f=open("a.txt")
    data=f.read()
    print(data)
    f.close
