import random, string, time

scores = {}
h=0

def split(word): 
    return [char for char in word]  

def game():
    g=[]
    consonants = ["B", "B", "C", "C", "C", "D", "D", "D", "D", "D", "D", "F", "F", "G", "G", "G", "H", "H", "J", "K", "L", "L", "L", "L", "L", "M", "M", "M", "M", "N", "N", "N", "N", "N", "N", "N", "N", "P", "P", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "S", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "T", "T", "T", "V","W", "X", "Y","Z"]
    vowels = ["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","I","I","I","I","I","I","I","I","I","I","I","I","I","O","O","O","O","O","O","O","O","O","O","O","O","O","U","U","U","U","U",]
    words = []
    take = []
    wordlength = 3
    g=[]
                                                                                                                    
                                                                                     
    letters = []
    random.shuffle(vowels)
    random.shuffle(consonants)

    for i in range(9): 
        which = input("Vowel or consonant?").lower()
        if which == "c" or which == "consonant":
            choose = consonants[0].lower()
            print (choose,"\n")
            letters.append(choose)
            print (" ".join(map(str,letters)),"\n")
            consonants.remove(consonants[0])
        elif which ==  "v" or which == "vowel":
            choose = vowels[0].lower()
            print (choose,"\n")
            vowels.remove(vowels[0])
            letters.append(choose)
            print (" ".join(map(str,letters)),"\n")
            vowels.remove(vowels[0])

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
            
    with open("C:\\Users\saulw\Documents\Python\Projects\Countdown\Letters game\wordswords.py") as f:
        for line in f.readlines():
            #print (line)
            for word in line.split():
                if len(word)<10 and len(word)>2:
                    betters=letters.copy()
                    word = split(word)
                    length = len(word)
                    for i in word:
                        length = length-1
                        if i not in betters:
                            break
                        else:
                            betters.remove(i)
                            if length==0:
                                wordjoin = ''.join([str(elem) for elem in word]) 
                                g.append(wordjoin)
                            

    print (len(g))
    f.close()          

    for i in scores: 
        print (i)
        word = input("What was your word?")
        if word in g:
            print ("Well done, you got",len(word),"points","\n")
            scores[i]=scores[i]+len(word)
            
        else:
            print("Sorry, not a real word that can be made with these letters","\n")


    time.sleep(3)

    g.sort(key = lambda s: len(s))
    g.reverse()

    thelong = (len(g[0]))
    print ("The longest word was", thelong, "letters long")

    for i in g:
        if len(i) == thelong:
            print (i.capitalize())
        else:
            break
        
    thelong=thelong-1
    print ("You could have also found words which are", thelong, "letters long such as:")
    for i in g:
        if len(i) == thelong:
            print (i.capitalize())

    print ("SCORES:")
    for i in (scores):
        print (i,scores[i])

    
        
    
rounds = int(input("How many rounds do you want to play?"))
players = int(input("How many players are involved?"))
              
for i in range (players):
              name = input("Input player name")
              scores[name] = 0
              

    
print (scores)

for i in range(rounds):
    game()





