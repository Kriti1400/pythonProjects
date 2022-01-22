decimal=0
#decimal represents the float the user enters
decimal1=0
#decimal1 represents the float the user enters
add=0
#add represents the sum of all the decimals
large=0
#large represents the largest float
for c in range(10):
    decimal=float(input("Enter a float:"))
    add=add+decimal 
    if decimal>decimal1:
        large=decimal
        print (large)
        decimal1=decimal
    print ("Sum is:",add)
print ("The average is",add/10)
print ("The largest number is:",large)
