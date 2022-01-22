import random
ace=0
#heads represents the number of times an ace of spades was shuffled
card=0
#card represents what the output is when the deck is shuffled
total=0
#total repreesents the number of times the deck was shuffled
while ace!=5:
    card=random.randrange(52)+1
    print (card)
    total=total+1
    if card==1:
        ace=ace+1
print("Stimulations:",total)

    

    
