fhand = open('mbox.txt')
count=0
for line in fhand:
    words = line.split()
    #print ('Test:', words)
    if len(words)==0 : continue
    if words[0]!='From': continue
    count+=1
    print (words[1])
print (count)
