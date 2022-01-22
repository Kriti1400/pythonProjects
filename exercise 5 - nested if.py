salary=float(input("Enter an annual salary:"))
#salary represents the annual salary entered by the user
print (salary)
if salary>50000:
    print ("Income tax for the annual salary of $",salary,"is $",(salary*0.35))
elif salary>=20000 and salary<=50000:
    print ("Income tax for the annual salary of $",salary,"is $",(salary*0.30))
elif salary>=6000 and salary<20000:
        print ("Income tax for the annual salary of $",salary,"is $",(salary*0.25))
else:
    print ("No income tax can be calculated")
