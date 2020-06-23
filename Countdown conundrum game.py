import random,time
g=[]
with open("C:\\Users\saulw\Documents\Python\Projects\Countdown\Letters game\wordswords.py") as f:
        for line in f.readlines():
            for word in line.split():
                if len(word)<10 and len(word)>8:
                    g.append(word)
f.close()
gosh = random.randint(0,len(g))
letters=g[gosh]
l = list(letters)
random.shuffle(l)
wordjoin = ''.join([str(elem) for elem in l])
print (wordjoin)
print ("READY")
time.sleep(3)
print ("SET")
time.sleep(3)
print ("GO!")
countdown =30

now = time.time()
future = now + countdown
while time.time() < future:
    now = time.time()
    greg = (round(future-now,0))
    now = time.time()
    if greg != round(future-now,0):
        print (greg)

ans = input("What was your answer?")
if ans in g:
    print ("Well done")
else:
    print ("Wrong, sorry. The answer was", g[gosh])
