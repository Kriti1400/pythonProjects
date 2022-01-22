second=0
#second represents the seconds on the stopwatch
minute=0
#minute represents the minutes on the stopwatch
hour=0
#hour represents the hours on the stopwatch
while hour!=60:
    while minute!=60:
        while second!=60:
            print (second)
            print ("\t",minute)
            print ("\t\t",hour)
            second=second+1
        second=0
        minute=minute+1
    minute=0
    hour=hour+1
            
