
from pyrogram import Client
import time
import sys

print("""


    Coded by erfan4lx

    Contact with Email : erfn4lx@gmail.com
    Contact with Telegram : @erfan4lx

    Made by : M4nifest0 , Unidentified , Vortex Cyber Security Team

    Happy Hacking ;))))

""")
time.sleep(5)

alf = open("Sessions.txt","r").read()
alf1 = alf.split()

i = 1
j = 0

while True:
    try:
        a = str(alf1[j])
        b = int(alf1[j+1])
        c = str(alf1[j+2])
        d = str(alf1[j+3])
    except:
        print("Finished")
        sys.exit()
    app = Client("Sessions/"+a,b,c,phone_number=d)
    app.start()
    app.send_message("me",str(i))
    app.stop()
    print("Session "+str(i)+" Created !")
    i += 1
    j += 4

print("""


    Coded by erfan4lx

    Contact with Email : erfn4lx@gmail.com
    Contact with Telegram : @erfan4lx

    Made by : M4nifest0 , Unidentified , Vortex Cyber Security Team

    Happy Hacking ;))))

""")
time.sleep(5)
sys.exit()

