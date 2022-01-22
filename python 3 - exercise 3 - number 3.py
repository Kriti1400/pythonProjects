mark1=int(input("Enter the first mark:"))
#mark1 represents the first mark entered by the user
mark2=int(input("Enter the second mark:"))
#mark2 represents the second term entered by the user
mark3=int(input("Enter the third mark:"))
#mark3 represents the third mark entered by the user
mark4=int(input("Enter the fourth mark:"))
#mark4 represents the fourth term entered by the user
mark5=int(input("Enter the fifth mark:"))
#mark5 represents the fifth mark entered by the user
mark6=int(input("Enter the sixth mark:"))
#mark6 represents the sixth term entered by the user
mark7=int(input("Enter the seventh mark:"))
#mark7 represents the seventh mark entered by the user
mark8=int(input("Enter the eighth mark:"))
#mark8 represents the eighth term entered by the user
total=0
#total represents the sum of the sequence
if mark1>-1 and mark2>-1 and mark3>=1 and mark4>-1 and mark5>-1 and mark6>-1 and mark7>-1 and mark8>-1 and mark1<101 and mark2<101 and mark3<101 and mark4<101 and mark5<101 and mark6<101 and mark7<101 and mark8<101:
    if mark1>mark2 and mark1>mark3 and mark1>mark4 and mark1>mark5 and mark1>mark6 and mark1>mark7 and mark1>mark8:
        print ("Highest mark:",mark1)
    elif mark2>mark1 and mark2>mark3 and mark2>mark4 and mark2>mark5 and mark2>mark6 and mark2>mark7 and mark2>mark8:
        print ("Highest mark:",mark2)
    elif mark3>mark1 and mark3>mark2 and mark3>mark4 and mark3>mark5 and mark3>mark6 and mark3>mark7 and mark3>mark8:
        print ("Highest mark:",mark3)
    elif mark4>mark1 and mark4>mark3 and mark4>mark2 and mark4>mark5 and mark4>mark6 and mark4>mark7 and mark4>mark8:
        print ("Highest mark:",mark4)
    elif mark5>mark1 and mark5>mark3 and mark5>mark4 and mark5>mark2 and mark5>mark6 and mark5>mark7 and mark5>mark8:
        print ("Highest mark:",mark5)
    elif mark6>mark1 and mark6>mark3 and mark6>mark4 and mark6>mark5 and mark6>mark2 and mark6>mark7 and mark6>mark8:
        print ("Highest mark:",mark6)
    elif mark7>mark1 and mark7>mark3 and mark7>mark4 and mark7>mark5 and mark7>mark6 and mark7>mark2 and mark7>mark8:
        print ("Highest mark:",mark7)
    elif mark8>mark1 and mark8>mark3 and mark8>mark4 and mark8>mark5 and mark8>mark6 and mark8>mark7 and mark8>mark2:
        print ("Highest mark:",mark8)
    if mark1<mark2 and mark1<mark3 and mark1<mark4 and mark1<mark5 and mark1<mark6 and mark1<mark7 and mark1<mark8:
        print ("Lowest mark:",mark1)
    elif mark2<mark1 and mark2<mark3 and mark2<mark4 and mark2<mark5 and mark2<mark6 and mark2<mark7 and mark2<mark8:
        print ("Lowest mark:",mark2)
    elif mark3<mark2 and mark3<mark1 and mark3<mark4 and mark3<mark5 and mark3<mark6 and mark3<mark7 and mark3<mark8:
        print ("Lowest mark:",mark3)
    elif mark4<mark2 and mark4<mark3 and mark4<mark1 and mark4<mark5 and mark4<mark6 and mark4<mark7 and mark4<mark8:
        print ("Lowest mark:",mark4)
    elif mark5<mark2 and mark5<mark3 and mark5<mark4 and mark5<mark1 and mark5<mark6 and mark5<mark7 and mark5<mark8:
        print ("Lowest mark:",mark5)
    elif mark6<mark2 and mark6<mark3 and mark6<mark4 and mark6<mark5 and mark6<mark1 and mark6<mark7 and mark6<mark8:
        print ("Lowest mark:",mark6)
    elif mark7<mark2 and mark7<mark3 and mark7<mark4 and mark7<mark5 and mark7<mark6 and mark7<mark1 and mark7<mark8:
        print ("Lowest mark:",mark7)
    elif mark8<mark2 and mark8<mark3 and mark8<mark4 and mark8<mark5 and mark8<mark6 and mark8<mark7 and mark8<mark1:
        print ("Lowest mark:",mark8)
    else:
        print ("Please enter all different numbers")
else:
    print ("Invalid input")
total=mark1+mark2+mark3+mark4+mark5+mark6+mark7+mark8
print ("Average:",total/8)
