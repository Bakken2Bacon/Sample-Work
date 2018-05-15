fname = input ('Enter file name:')
count=0
total=0
average=0
try:
    fhandle=open(fname)
    #print (fhandle,"\n")
    for line in fhandle:
        #goes through each LINE in the opened file
        #if the line starts with the below then it strips
        if line.startswith('X-DSPAM-Confidence:'):
            #this gives us the actual INDEX value of that :. but we want everything after that colon
            semi=line.find(':')
            num=line[semi+1:]
            num=float(num)
            total=float(total)+num
            count=count+1
    average = total/count
    #average=str(average)
    #ths limits it to just 10 characters and average is a STRING!!!!!!
    #average = average [:10]
    print ("Count:",count)
    print ("Total",total)
    print ("Average Spam Confidence:", average)


                       #numbers=newline[:]

            #print(line)

except:
    print ('error')
