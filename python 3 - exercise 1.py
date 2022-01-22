price=float(input("Enter the price of an item:"))
#price represents the price entered by the user
print (price)
response=input("Do you wish to continue (y/n)?")
print (response)
#respose represents the response of the user
while response!="n":
    price2=float(input("Enter the price of an item:"))
    #price2 represents the continuation in price
    price=price+price2
    print (price)
    response=input("Do you wish to continue (y/n)?")
    print (response)
print ("subtotal is $",price)
print ("HST is $",price*0.13)
print ("total price is $",price+(price*0.13))









