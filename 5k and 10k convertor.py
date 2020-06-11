print ("enter your most recent 5k time")
mins = 0
seconds = 0
while mins == 0:
    try:
        mins = int(input("How many minutes"))
    except:
        print ("That's not a number, please enter an integer")
while seconds == 0:
    try:
        seconds = int(input("How many seconds"))
    except:
        print ("That's not a number, please enter an integer")
        
seconds += mins *60


overall = ((seconds *(10/5)**1.06))

mins = overall/60
seconds = overall%60

print ("Your 10k time would be", round(mins), "minutes and", round(seconds), "seconds")
