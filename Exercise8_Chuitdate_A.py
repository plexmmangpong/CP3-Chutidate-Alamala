username = input("Username : ")
password = input("Pasword : ")
if username == "pleum" and password == "1234":
    print("Success")
    print(f"[---Wellcome {username} ---]")
    print("1.Mac Pro M3 : 79,900 ฿")
    print("2.Mac Air M3 : 39,900 ฿")
    while True:
        select = int(input(">>"))
        if select == 1:
            product = "Mac Pro M3"
            price = 79900
            break
        
        elif select == 2:
            product = "Mac Air M3"
            price = 39900
            break
        
        else :
            print("Please Enter 1-2")
            continue
        
    print(f"\n\n{product}\nprice : {price:,}฿")    
    amount = int(input("Enter amount you want : "))
    
    print(f"\n\n{product} x{amount:,}\n{amount*price:,}฿")
    print("Succes!your order will be delivered in 3 days.") 
        
else :
    print("Invalid email or password")
    
    
