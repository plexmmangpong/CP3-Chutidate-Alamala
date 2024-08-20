import os

def clearscreen():
    os.system("cls")
    
def login():
    while True:
        clearscreen()
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
        if usernameInput == "admin" and passwordInput == "1234":
            return "Done!",Menu()
        else:
            print("Invaild Gmail or password!")
            continue
         
def Menu():
    clearscreen()   
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    Menu_Selected()
    
def Menu_Selected():     
    userSelected = int(input(">>"))
    if userSelected == 1:
        clearscreen()
        print(VatCaculation(int(input("Enter Price(TH-Baht):"))),"฿")
        
    if userSelected == 2:
        print(Price(),"฿")
                     
def VatCaculation(price):
    vat = 7
    result = price + (price * vat / 100)
    return result
       
def Price():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return VatCaculation(price1+price2)
    
login()    
