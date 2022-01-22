import random
rolls=int(input("Enter the number of rolls:"))
#rolls represents the number of times the user wants to roll
for c in range(rolls,0,-1):
    print (random.randrange(6)+1)
print ("1:
