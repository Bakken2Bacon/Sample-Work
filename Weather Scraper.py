'''8/13/17 Functional and personalized python projects - this program would scrape the Des Moines website to
gather information on
the weather for the week (or day....can manipulate code as necessary'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sqlite3
conn = sqlite3.connect('weather.db')
cur = conn.cursor()
import time
## dd/mm/yyyy format
currentdate=time.strftime("%d/%m/%Y")
# Create table

cur.execute('''CREATE TABLE IF NOT EXISTS DSM_Temperature
                (Days DATE, T TEXT, Temp TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://www.kcci.com/weather', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
degree_sign= u'\N{DEGREE SIGN}'
#print (degree_sign)
# Retrieve all of the anchor tags
tempend=soup.find(class_="hourly-forecast open")

curt=soup.find(class_="weather-page-detail--current-temp-value")
curc=soup.find(class_="weather-page-detail--current-condition")
temp_now=list()
for ind in curt,curc:
    for solo in ind:
        temp_now.append(solo)
print ("Current temperature and conditions in Des Moines Right now:", temp_now)

#print (tempend)
t1=list()
t2=list()
t3=list()
di={}
final={}
for text in tempend:
    for x in text:
        #print(x.split)
        for z in x:
            try:
                #print (z.split())
                t1.append(z)
                if degree_sign in z:
                    t2.append(z)
                elif 'M' in z:
                    t3.append(z)
            except:
                continue
            #if degree_sign in z:
            #    t1.append(z)

##******
# Insert a row of data
# count=0
# # while count<len(t2):
# #         x="UPDATE DSM_Temperature(Day) VALUES (?); " % currentdate
# #         cur.execute(x)
# #         count+=1
#         #print (count)

#t3 is the time not the temperature
z=list(zip(t2,t3))
print(z)
for d in z:
    cur.execute('INSERT INTO DSM_Temperature (Temp, T) VALUES (?, ?)', d)
    conn.commit()
#
# # Save (commit) the change
cur.execute('UPDATE DSM_Temperature (Days) VALUES (currentdate)')
conn.commit()
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
conn.close()



#********
#print('t1',t1)
#print('t2',t2)
#print('t3',t3)
#di=dict(zip(t2,t3))
#print ('this is di',di)
#for key, value in di.items() :
    #print (key, value)
#    final[value]=key
#print(final)
cool=list(zip(t3,t2))
#print(cool)

# while True:
#     user=input('Enter a time, and I will give you the temperature: ')
#     try:
#         if len(user)<1 or user=="done":
#             break
#         else:
#             try:
#                 ind=t3.index(user)
#                 print("The temperature in Des Moines at that time is:", t2[ind])
#             except:
#                 ind=t3.index(user)
#                 print(t2[ind])
#     except:
#         print ("Invalid time, try again, or leave it blank, or type 'done' to exit ")
#         continue
#FUNCTIONAL - 8/13/2017 - 8:30 AM!
