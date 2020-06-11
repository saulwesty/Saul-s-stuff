import random,operator
rounds = ["Phase 1: 2 sets of 3",
"Phase 2: 1 set of 3 + 1 run of 4",
"Phase 3: 1 set of 4 + 1 run of 4",
"Phase 4: 1 run of 7",
"Phase 5: 1 run of 8",
"Phase 6: 1 run of 9",
"Phase 7: 2 sets of 4",
"Phase 8: 7 cards of one color",
"Phase 9: 1 set of 5 + 1 set of 2",
"Phase 10: 1 set of 5 + 1 set of 3"]
score =0

scores = {"Dad":0, "Saul":0,"Mum":0,"Jut":0,}
k=1
random.shuffle(rounds)  

for i in rounds:
    print ("Round",k,i)
    k+=1
for i in rounds:
    print ("\n",i)  
    print ("Please input each player's score")
    for j in scores:
        while not score:
            try:
                score = int(input(j))
                if score == 0:
                    break
            except:
                print ("That is not a number, please input an integer")
        scores[j] +=score
        score =0
    sorted_dicz = sorted(scores.items(), key=operator.itemgetter(1))
    for i in reversed(sorted_dicz):
        print (i[0],i[1]) 
  

sorted_dicz = sorted(scores.items(), key=operator.itemgetter(1))

print ("Well done", sorted_dicz[0][0], "you win")


#to solve problem do if else with the try loop in else part

