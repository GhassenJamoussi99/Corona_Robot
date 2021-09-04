from tkinter import *
from KeypadControlPC import *
from urllib.request import urlopen
from Line_Follower import follow
import base64
from threading import *
from cam_streaming.webstreaming import videostreaming
from audio.amg88_temp import *

def threading1():
    t1=Thread(target=videostreaming)
    t1.start()

def threading2():
    t2=Thread(target=temp_audio)
    t2.start()

app = Tk()
app.title("Controlling Interface")
app.geometry("600x1000")


img_url = "https://i.imgur.com/sdS4zeN.png"
img_byt = urlopen(img_url).read()
img_b64 = base64.encodestring(img_byt) 
photo = PhotoImage(data=img_b64)
w = Label(app, image=photo)
w.pack()
ent = Entry(app)

welcome=Label(app,text="\nRobot Interface\n")
welcome.config(font=('tahoma',15,'bold'))
welcome.pack()


myButton = Button(app, text="Keyboard", command=Keyboard)
myButton.place(relx=0.5, rely=0.5, anchor=CENTER)
myButton.pack()

space=Label(app,text="\n")
space.config(font=('tahoma',2,'bold'))
space.pack()

myButton = Button(app, text="Line Follower", command=follow)
myButton.place(relx=0.5, rely=0.5, anchor=CENTER)
myButton.pack()

space=Label(app,text="\n")
space.config(font=('tahoma',2,'bold'))
space.pack()

myButton = Button(app, text="Video streaming", command=threading1)
myButton.place(relx=0.5, rely=0.5, anchor=CENTER)
myButton.pack()

space=Label(app,text="\n")
space.config(font=('tahoma',2,'bold'))
space.pack()

myButton = Button(app, text="Detect temperatures", command=threading2)
myButton.place(relx=0.5, rely=0.5, anchor=CENTER)
myButton.pack()


space=Label(app,text="\n\nDeveloped by:\nGhassen Jamoussi\nWadi Touil")
space.config(font=('italic',12,'bold'))
space.pack()

space=Label(app,text="\n© All rights are reserved to those 2 developers")
space.pack()

app.mainloop()
