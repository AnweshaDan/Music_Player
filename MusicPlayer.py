import os
from tkinter import filedialog
from tkinter import *
from pygame import mixer
import tkinter.messagebox



root = Tk()

mixer.init()  

root.geometry('300x300')
root.title("Music")#later

statusbar=Label(root,text='Welcome!',relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)


leftframe=Frame(root)
leftframe.pack(side=LEFT,padx=30)

rightframe=Frame(root)
rightframe.pack()

topframe=Frame(rightframe)
topframe.pack()
middleframe=Frame(rightframe)
middleframe.pack()
bottomframe=Frame(rightframe)
bottomframe.pack()

menubar=Menu(root)
root.config(menu=menubar)

submenu=Menu(menubar,tearoff=0)

plist=[]

def browse_files():
    global f
    global filename_path
    filename_path=filedialog.askopenfilename()
    f=os.path.basename(filename_path)
    add_to_playlist()
    
def add_to_playlist():
    index=0
    playlist.insert(index,f)
    plist.insert(index,filename_path)
    index+=1
    print(plist)
    

menubar.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Open',command=browse_files)
submenu.add_command(label='Exit',command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('About us','Listen to your favourite music whenever you want.')

submenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=submenu)
submenu.add_command(label='About us',command=about_us)

playlist=Listbox(leftframe)
playlist.pack()

addbtn=Button(leftframe,text="Add.",command=browse_files)
addbtn.pack(side=LEFT)

def del_song():
    selected_song=playlist.curselection()
    selected_song=int(selected_song[0])
    playlist.delete(selected_song)
    plist.pop(selected_song)
    print(plist)

rmvbtn=Button(leftframe,text="Remove.",command=del_song)
rmvbtn.pack(side=LEFT)


text = Label(topframe, text='Lets make some noise!')
text.pack()



    
def stop_music():
    mixer.music.stop()
    statusbar['text']="Music stopped."
    
def pause_music():
    global paused
    paused=True
    mixer.music.pause()
    statusbar['text']="Music paused."
    
def play_music():
    try:
        paused
    except NameError :
        try :
            selected_song=playlist.curselection()
            selected_song=int(selected_song[0])
            play_it=plist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text']="Playing "+ os.path.basename(play_it)
        except :
            tkinter.messagebox.showerror('Error','No songs in the playlist')
    else:
        mixer.music.unpause()
        statusbar['text']="Music resumed."

def set_vol(val):
    volume= int(val)/100
    mixer.music.set_volume(volume)


playPhoto = PhotoImage(file='touch.png')
playBtn = Button(middleframe, image=playPhoto, command=play_music)
playBtn.pack(side=LEFT)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.pack(side=LEFT)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.pack()

scale=Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()


root.mainloop()