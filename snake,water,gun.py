import random

def check(user, comp):
    if user == comp:
        return "DRAW"
    
    if (user == 1 and comp == 2) or \
       (user == 2 and comp == 3) or \
       (user == 3 and comp == 1):
        return "USER WON"
    else:
        return "COMPUTER WON"

while True:
    x = input("Press Q to exit or Enter to play: ")
    if x.upper() == "Q":
        print("Thanks for playing! 👋")
        break
        
    user = int(input("1 for Snake, 2 for Water, 3 for Gun: "))
    if(user>3):
         print("invalid")
         break
    
    comp = random.randint(1, 3)

    if(user==1):
        user = "SNAKE"
    if(user==2):
        user = "WATER"
    if(user==3):
        user = "GUN"
    if(comp==1):
        comp = "SNAKE"
    if(comp==2):
        comp = "WATER"
    if(comp==3):
        comp = "GUN"
    print(f"You choose {user}, Computer choose {comp}")
    if(user=="SNAKE"):
          user=1
    if(user=="WATER"):
          user=2
    if(user=="GUN"):
          user=3
    if(comp=="SNAKE"):
          comp=1
    if(comp=="WATER"):
          comp=2
    if(comp=="GUN"):
          comp=3
    print(check(user, comp))
    print("-" * 30)
