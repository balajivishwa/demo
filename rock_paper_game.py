import random


def play():
 user = input("P for paper, R for rock and S for seccors \n")

 computer = random.choice(["R","P","S"])
 if(user==computer):
     print(f"both the players has chosen the ${user}, so draw")
 elif(user=="P" & computer=="s"|user=="R" & computer=="P"|user=="S" & computer=="R") :
     print("COMPUTER WON THE MACH !!") 
 else:
     print("the user won the macth!!") 

play()
