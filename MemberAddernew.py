
from pyrogram import Client
import time
import sys

print("""


  telegram bot

""")
time.sleep(5)

print("""\n\n
 Do you need to add members from your specific group ENTER 1
 Or
 Add with your destination usernames list ENTER 2
""")

orginally = int(input("Type number 1 or 2: "))

alf = open("Sessions.txt","r").read()
alf1 = alf.split()
lena = len(alf1)
threads = int(lena/4)

app0 = Client("Sessions/"+str(alf1[0]),int(alf1[1]),str(alf1[2]),str(alf1[3]))
app1 = Client("Sessions/"+str(alf1[4]),int(alf1[5]),str(alf1[6]),str(alf1[7]))
app2 = Client("Sessions/"+str(alf1[8]),int(alf1[9]),str(alf1[10]),str(alf1[11]))
app3 = Client("Sessions/"+str(alf1[12]),int(alf1[13]),str(alf1[14]),str(alf1[15]))


apps = [app0 ,app1 ,app2 ,app3]

for app in apps:
    app.start()

aaaaaa = len(apps)

class GroupToGroup_AddMember():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1, Link2):
            global a,b
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id
            self.Group_ChatID = app0.get_chat(Link2)
            b = self.Group_ChatID.id

    def Add_To_Group(self, Source, Destination):
        members = app0.iter_chat_members(Source)
        counter = 1
        ccc = 1
        for index, member in enumerate(members):
            app = apps[index % threads]
            print(str(app))
            try:
                user_id = member.user.username
                app.add_chat_members(Destination, user_id)
            except:
                pass
            else:
                print("Added "+str(counter)+" "+str(user_id)+"\t"+str(ccc))
                counter = counter+1
                ccc += 1
            if str(ccc) == str(aaaaaa):
                ccc = 1
                time.sleep(900)

class GroupToGroup_AddMember1():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1):
            global a
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id

    def Add_To_Group(self, Destination):
        counter = 1
        limits = 0
        for index, member in enumerate(members):
            app = apps[limits]
            limits += 1
            print(str(app))
            ccc = 1
            try:
                app.add_chat_members(Destination, member)
            except:
                pass
            else:
                print("Added "+str(counter)+" "+str(member)+"\t"+str(ccc))
                counter = counter+1
                ccc += 1
            if str(ccc) == str(aaaaaa):
                ccc = 1
                
            if limits == threads:
                limits = 0
                time.sleep(1500)
                
if int(orginally) == 1:
    one = input("Source group: ")
    two = input("Destination group: ")

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    if "@" in str(two):
        twoo = two.replace("@","")
    else:
        twoo = two
    try:
        for app in apps:
            app.join_chat(str(onee))
            app.join_chat(str(twoo))
    except:
        pass

    App_Start = GroupToGroup_AddMember()
    ab = App_Start.Get_group_chat_id(one, two)
    App_Start.Add_To_Group(a, b)

elif int(orginally) == 2:
    one = input("Destination group: ")
    members1 = str(input("Enter your file of members: "))

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    try:
        for app in apps:
            app.join_chat(str(onee))
    except:
        pass

    members = open(members1 , "r").read()
    members = members.split()
    App_Start = GroupToGroup_AddMember1()
    ab = App_Start.Get_group_chat_id(one)
    App_Start.Add_To_Group(a)
else:
    for app in apps:
        app.stop()
    sys.exit("Enter 1 or 2")

print("""


Telegram bot

""")

time.sleep(5)
for app in apps:
    app.stop()
sys.exit()

