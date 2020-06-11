import operator

dicz = {"Belgium": [0,0,0], "Panama": [0,0,0], "England": [0,0,0], "Tunisia": [0,0,0]}

listz = ["Belgium", "Panama", 3, 0, "Tunisia", "England", 1, 12, "Belgium", "Tunisia", 5,2, "England", "Panama", 6,1,"England", "Belgium", 0,1,"Panama", "Tunisia", 2,2]

while len(listz)>0:
    if listz[2]>listz[3]:
        dif = listz[2]-listz[3]
        for i in dicz:
            if listz[0]==i:
                dicz[i][0] +=3
                dicz[i][2] += listz[2]
                dicz[i][1] += dif
            if listz[1]==i:
                dicz[i][2]+=listz[3]
                dicz[i][1] -= dif
    elif listz[2]<listz[3]:
        dif = listz[3]-listz[2]
        for i in dicz:
            if listz[1]==i:
                dicz[i][0] +=3
                dicz[i][2] += listz[3]
                dicz[i][1] += dif
            if listz[0]==i:
                dicz[i][2]+=listz[2]
                dicz[i][1] -= dif
    else:
        for i in dicz:
            if listz[0]==i:
                dicz[i][0] +=1
                dicz[i][2] += listz[2]
            if listz[1]==i:
                dicz[i][0] +=1
                dicz[i][2] += listz[2]
    del listz[0:4]

    

sorted_dicz = sorted(dicz.items(), key=operator.itemgetter(1))

#for i in sorted_dicz

print ("Team    P GD G")
for i in reversed(sorted_dicz):
    print (i[0],i[1][0],i[1][1],i[1][2])
    
    


    

