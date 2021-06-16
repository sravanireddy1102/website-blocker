import time
from datetime import datetime as dt
hosts_path='C:\Windows\System32\drivers\etc\hosts'
redirect='127.0.0.1'

websites=['www.instagram.com','www.netflix.com','facebook.com','twitter.com']
while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,22)):
        print("working hours :)")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)#goes to the beginning of the file.
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(10)





