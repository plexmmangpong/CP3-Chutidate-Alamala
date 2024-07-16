import os

def clearscreen():
    os.system("cls")

Found_ENG = float(input("Enter Foundation English Score : ")) 
Gen_Buss  = float(input("Enter General Bussiness : "))
Com_Sys   = float(input("Enter Introduction to Computer Systems : ")) 
Com_Prog  = float(input("Enter Computer Programming : "))

clearscreen()

print("--- Your Score ---")
print(f"Foundation English : {Found_ENG}")
print(f"General Business   : {Gen_Buss}")
print(f"Introduction to Computer Systems : {Com_Sys}")
print(f"Computer Programming : {Com_Prog}")
 
