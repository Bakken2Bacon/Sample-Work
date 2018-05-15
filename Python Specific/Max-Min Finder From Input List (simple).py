num=[]
while True:
    x=input("Enter a number or type done if no more:" )
    if x == 'done' or len(x)<1:
        break
    elif x!='done':
        num=num+[x]

mx=[float(i) for i in num]
mx.sort()
print (mx)
print ("max :", max(mx))
print ("min :", min(mx))