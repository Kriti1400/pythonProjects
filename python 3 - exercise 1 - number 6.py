mark=int(input("Enter a mark"))
#mark represents the mark the user enters
print (mark)
mark2=0
#mark2 represents all the marks entered after the first
times=0
#times represents the number of times the mark was entered
while mark>-1 and mark2>-1:
    mark2=int(input("Enter a mark"))
    mark=mark+mark2
    print (mark)
    times=times+1
    print (times)
print ("Average is:",mark/times)
