import requests
import sqlite3
from bs4 import BeautifulSoup
conn = sqlite3.connect('course.db')
c = conn.cursor()
res = requests.get('https://babu7.github.io/2.html')
soup = BeautifulSoup(res.text, "html")


a = soup.select('tr')
for test in soup.select('tr'):
  k=1
  temp=''
  aa=[]
  for i in test.select('td'):
    if(k!=1 and k!=8):
      aa.append(i.text.split('\r\n')[0])
      k+=1
    else:
      k+=1
  if len(aa)!=0:
    for l in range(len(aa)):
      if aa[l]=="":
        aa[l]="null"
    temp+='\''+aa[6]+'\''+','+'\''+aa[5]+'\''
    for p in range(5):
      if '\'' in aa[p]:
        tempaa=aa[p].split('\'')
        aa[p]=tempaa[0]+tempaa[1]
      temp = temp + ','+'\''+aa[p]+'\''
    c.execute("INSERT INTO course (teacher,course,department,star,a,b,c) \
     VALUES ("+temp+" )")
conn.commit()
conn.close()
