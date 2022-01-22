import random
rolls=int(input("Enter the number of rolls:"))
#rolls represents the number of times the die was rolled
one=0
#one represents the number of times one was rolled
two=0
#two represents the number of times two was rolled
three=0
#three represents the number of times three was rolled
four=0
#four represents the number of times four was rolled
five=0
#five represents the number of times five was rolled
six=0
#six represents the number of times six was rolled
die=0
#die represents the roll of the die
for c in range(rolls):
    die=random.randrange(6)+1
    if die==1:
        one=one+1
    elif die==2:
        two=two+1
    elif die==3:
        three=three+1
    elif die==4:
        four=four+1
    elif die==5:
        five=five+1
    else:
        six=six+1
for c in range(rolls):
    die=random.randrange(6)+1
    if die==1:
        one=one+1
    elif die==2:
        two=two+1
    elif die==3:
        three=three+1
    elif die==4:
        four=four+1
    elif die==5:
        five=five+1
    else:
        six=six+1
print ("one:",one)
print ("two:",two)
print ("three:",three)
print ("four:",four)
print ("five:",five)
print ("six:",six)

