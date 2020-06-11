import time
import datetime
k=0

def stopwatch():
    k=0
    count = 0
    while count == 0:
        count = input("Type Yes to start the stopwatch or No to exit").lower()
        if count == "yes" or count == "y":
            pass
        elif count == "n" or count == "no":
            print ("OK, thanks for using my programme")
            exit()
        else:
            count = 0
            print ("This is not valid, please enter yes or no")
    
    was = time.time()
    while k<1:
        now = time.time()
        summ = (round(now-was,2))
        #print (summ)
        stop = input("Stop? Yes or no?").lower()
        if stop == "y" or stop == "yes":
            k=1
            now = time.time()
            print ("Your time was:")
            print (round(now-was,4))
        k+=0.0001
        


    
def clock():
    k=-1
    
    while k<0:
        datetime_object = str(datetime.datetime.now())
        date = datetime_object.split()
        which = input("Which country would you like the time in? UK or Israel?").lower()
        if which == "uk" or which == "united kingdom" or which == "great britain":
            print ("The date is", date[0])
            print ("The time is currently", date[1])
            k=0
        elif which == "israel":
            some = int(date[0][1])
            some += 2
            some = str(some)
            date[1] = date[1][:1] + some + date[1][2:]
            print ("The date is", date[0])
            print ("The time is currently", date[1])
            k=0
        else:
            print ("Please input one of the valid countries, Israel or UK")


    
def timer():
    countdown = 0
    while not countdown:
        try:
            countdown = int(input("How many seconds would you like counted down?"))
        except:
            countdown = 0
            print ("This isn't valid, please input a number")
    now = time.time()
    future = now + countdown
    while time.time() < future:
        now = time.time()
        print (round(future-now,2))



while k<1:
    k=+1
    which = input("Would you like to use the stopwatch, clock or timer feature").upper()
    if which == "S" or which == "STOPWATCH":
        stopwatch()
    elif which == "C" or which == "CLOCK":
        print ("Clock")
        clock()
    elif which == "T" or which == "TIMER":
        timer()
        print ("Time's up!")
    else:
        print ("This is not an option, please choose a feature")
        k=-1
        


