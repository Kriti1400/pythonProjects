LOGIN=631407
#LOGIN reresents my student number
PASSWORD=20030214
#PASSWORD represents my password
Login=int(input("Enter the login"))
#Login represents the login entered by the user
Password=int(input("Enter the password"))
#Password represents the password entered by the user
while Login!=LOGIN and Password!=PASSWORD:
    print ("Login Unsuccessful. Try Again.")
    Login=int(input("Enter the login"))
    Password=int(input("Enter the password"))
print ("Login Successful")
    


