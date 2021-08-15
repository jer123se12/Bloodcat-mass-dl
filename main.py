import requests
def download(url):
    x=requests.get(url)
    data=x.json()
    data2=[]
    for i in data["data"]:
        data2.append(str(i["SetId"]))
    data=data2
    path="./downloads/"
    for i in data:
        print("downloading"+i+"now")
        url="https://api.chimu.moe/v1/download/"+i+"?n=0"
        r = requests.get(url, allow_redirects=True)
        if r.content!="":
            with open(path+i+'.osz', 'wb') as a:
                a.write(r.content)
p=str(int(input("amt of files: "))-1)
o=input("offset")
o= o if len(o)>0 else 0
k=input("amt of keys: ")
if int(p)>100:
    for i in range(int(p)%100):
        if i>=0:
            o=0
        download(f"https://api.chimu.moe/v1/search?query=&mode=3&min_cs={k}&max_cs={k}&amount=100&offset={str(i+int(o))}00&status=1")
url=f"https://api.chimu.moe/v1/search?query=&mode=3&min_cs={k}&max_cs={k}&amount={str((int(p)%100))}&offset={o}"
download(url)
