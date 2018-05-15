fname = input('Enter File: ')
if len(fname)<1: fname='mbox.txt'
hand = open(fname)
di=dict()
for w in hand:
    #print ('old',w)
    w = w.rstrip()
    #print (w)
    wds = w.split()
    #print ('new',wds)
    for x in wds:
        #print (x)
        #print (wds) #keeps everything as a list but in a line still
        if 'From' not in x:
            continue
            #goes through each word and sees if from is there, if not it moves on.
        else:
            if len(wds)>2:
                print (wds)#eventually we get here where we have a list of the dates which is the 3rd set, but then we have to join them for hte ditionary
                y = "".join(wds[5:6])
                print (y)
                z=y.split()
                print ('this is z',z)
                for zz in z:
                    zy=zz[0:2]
                    print ('this is zz[0:2]',zy)
                #print(w)
                di[zy]=di.get(zy,0)+1
                #di[x]=di.get(x,0)+1
        #print (x, di[x])s
        #print (w,di[w])
        #di[line]=di.get(line,0)+1

print (di)
lis=list()
print('di',di.items())
for key,value in list(di.items()):
    #key=float(key)
    lis.append((key,value))
    lis.sort()
print (lis)
for key,value in lis:
    print (key,value)
