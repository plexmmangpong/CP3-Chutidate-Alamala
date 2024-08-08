def VatCaculator(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
print("\t(VAT CACULATOR)")
user = int(input("Enter Price : "))
print("TotalPrice >>",VatCaculator(user))


 
    