import random,time,datetime
from operator import add,mul,sub,truediv
ints = []
p=0
cole = 1000000
bignumbers = [75,25,100,50]
smallnumbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
operators = {"+": add, "-": sub, "*": mul,"/":truediv,}
keys=list(operators)
biz=[]
fiz = []
o=0
while o<1:
    try:
        big = int(input("How many big numbers do you want?"))
        o=+1
        if big<0 or big>4:
            o-=1
    except:
        print ("Please input an integer between 0 and 4")
        o-=1

small = 6-big
for i in range(small):
    random.shuffle(smallnumbers)
    ints.append(smallnumbers[0])
    smallnumbers.remove(smallnumbers[0])
for i in range(big):
    random.shuffle(bignumbers)
    ints.append(bignumbers[0])
    bignumbers.remove(bignumbers[0])
x=random.randrange(1,1000)
print (ints,"to get", x)
print ("READY")
time.sleep(3)
print ("SET")
time.sleep(3)
print ("GO!")
countdown=30  
now = time.time()
future = now + countdown
while time.time() < future:
    now = time.time()
    greg = (round(future-now,0))
    now = time.time()
    if greg != round(future-now,0):
        print (greg)

while p<100000: 
    intz=ints.copy()
    random.shuffle(intz)
    answer = intz[0]
    intz.remove(answer)
    biz.clear()
    biz.append(answer)
    for _ in range(4):
        number2 = intz[1]
        intz.remove(number2)
        operator = random.choice(keys)
        answer= (operators[operator](answer, number2))
        if float(answer).is_integer():
            pass
        else:
            break
        biz.append(operator)
        biz.append(number2)
        if answer == x:
            y=0
            while y<1:
                done = int(input("What was your score?"))
                if done == x:
                    print ("Congratulations, you got the same as me")
                else:
                    diff = abs(x-done)
                    print ("Unlucky, you were only", diff, "away")
                    y=+1
                see = input("Would you like to see how I did it?").lower()
                if see == "y" or see == "yes":
                    y=+1
                elif see == "n" or see == "no":
                    print ("Ok, thanks for playing")
                    exit()
                    y=+1
                else:
                    print ("Please input y or n")
                
                    
                    
            print ("\n")
            p=100004
            print ("NOTE: Bidmas does not apply below")
            print (" ".join(map(str, biz)))
            y=+1
            break
    whole = abs(answer-x)
    if whole<cole and float(answer).is_integer():
        fiz=biz.copy()
        bob = answer
        cole=whole

    
    p+=1
v = 0
if p != 100005:
    y=0 
    while y<1:
        while v<1:
            try:
                done = int(input("What was your score?"))
                v=+1
            except:
                print ("Please input an integer")
            
        diff = abs(done-x)
        mydiff = abs(bob-x)
        over = abs(mydiff-diff)
        
        if diff>mydiff:
            print ("Congratulations, you beat me by", diff)
        elif done == bob:
            print ("Well done, you got the same as me")
        else:
            if diff<mydiff:
                print ("Well done, you beat me by",over)
            elif mydiff<diff:
                print ("Unlucky, I beat you by", over)
            else:
                print ("I got that close too!")
        
        see = input("Would you like to see how I got there?").lower()
        if see == "y" or see == "yes":
            y=+1
        elif see == "n" or see == "no":
            print ("Ok, thanks for playing")
            exit()
            y=+1
        else:
            print ("Please input y or n")
    print ("NOTE: BIDMAS does not apply below")
    print (bob)
    print (" ".join(map(str, fiz)))  
 

















