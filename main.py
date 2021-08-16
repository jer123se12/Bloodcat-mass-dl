import requests
import threading
import time
from urllib.request import urlretrieve
import concurrent
def download(url,t):
    x=requests.get(url)
    data=x.json()
    data2=[]
    for i in data["data"]:
        data2.append(str(i["SetId"]))
    return data2
def d(data):
    path="./downloads/"
    threads=[]
    for i in data:
        starttime=time.time()
        url="https://api.chimu.moe/v1/download/"+i+"?n=0"
        threads.append(threading.Thread(target=dl2, args=(url,path,i)))
    active=[]
    for i in range(len(threads)):
        threads[i].start()
        active.append(i)
        if len(active)>t:
            for i in active:
                threads[i].join()
            active=[]
    for i in active:
        threads[i].join()
def dl2(url,path,i):
    starttime=time.time()
    print("downloading file with setid: "+i+" now")
    r = requests.get(url, allow_redirects=True)
    if len(r.content)>1:
        print("saving "+str(i)+" at: "+str(time.time()-starttime))
        with open(path+i+'.osz', 'wb') as a:
            a.write(r.content)
    print(str(i)+" done, time taken: "+str(time.time()-starttime))
    
p=str(int(input("amt of files: "))-1)
o=input("offset: ")
o= o if len(o)>0 else 0
k=input("amt of keys: ")
t=int(input("threads: "))
totalt=time.time()
data=[]
if int(p)>100:
    for i in range(int(p)//100):
        print(str(i)+"loaded out of "+str(int(p)//100))
        if i>=0:
            o=0
        data+=download(f"https://api.chimu.moe/v1/search?query=&mode=3&min_cs={k}&max_cs={k}&amount=100&offset={str((i*100)+int(o))}&status=1",t)

url=f"https://api.chimu.moe/v1/search?query=&mode=3&min_cs={k}&max_cs={k}&amount={str((int(p)%100))}&offset={o}"
print(url)
data+=download(url,t)
d(data)
print(f"DONE!!!!!\nTime take: {str(time.time()-totalt)}")
