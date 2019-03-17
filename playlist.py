print("********************Created by \"Sripranav Mannepalli\"********************")


import tkinter
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox
import os
import time
import threading
from pygame import mixer
from mutagen.mp3 import MP3
mixer.init()


window=tkinter.Tk()

window.iconbitmap('music.ico')

window.title("...MY-MUSIC...")

window.geometry("500x500")


left_frame=tkinter.Frame(window,relief="raised")
left_frame.pack(side="left")
right_frame=tkinter.Frame(window,relief="raised")
right_frame.pack(side="right")
top_frame=tkinter.Frame(right_frame,relief="sunken")
top_frame.pack()
mid_frame=tkinter.Frame(right_frame,relief="raised")
mid_frame.pack()
bot_frame=tkinter.Frame(right_frame,relief="raised")
bot_frame.pack()


p='0'
q='0'
b=' '
a=0
h=0
fin=0
ini=0
threadlist=[]
new_index=-5
thready=" "
vol=75
file_name=' '
new_file_name=' '
playlist_list=[]
index=0


def addto_playlist():
    global index
    global file_name
    file_name=filedialog.askopenfilename()
    f=file_name
    f=os.path.basename(f)
    f=f.split(".")
    f=f[:-1]
    playlist.insert(index,f)
    playlist_list.append(file_name)
    index+=1


def delfrom_playlist():
    try:
        dels=playlist.curselection()
        dels=int(dels[0])
        playlist_list.pop(dels)
        playlist.delete(dels)
        playlist.selection_clear(dels)
        mixer.music.stop()
    except:
        tkinter.messagebox.showerror("Error","Error")


playlist=tkinter.Listbox(left_frame)
playlist.pack()
but1=ttk.tkinter.Button(left_frame,text="+add",command=addto_playlist)
but1.pack(side="left")
but2=ttk.tkinter.Button(left_frame,text="-del",command=delfrom_playlist)
but2.pack(side="left")


menubar=tkinter.Menu(window)
window.config(menu=menubar)


sub_menubar1=tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(label="file",menu=sub_menubar1)
sub_menubar1.add_command(label="open",command=addto_playlist)


def about_me():
    tkinter.messagebox.showinfo('BEATS(playlist)','Developed by Sripranav Mannepalli')
def about_playlist():
    tkinter.messagebox.showinfo('BEATS(playlist)','This is a playlist , built using \'PYTHON 3\' with tkinter and')


sub_menubar2=tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(label="help",menu=sub_menubar2)
sub_menubar2.add_command(label='about creator',command=about_me)
sub_menubar2.add_command(label='about playlist',command=about_playlist)
sub_menubar2.add_command(label='exit',command=window.destroy)


bottom_most=tkinter.Label(window,text="Sripranav Mannepalli",relief="sunken",anchor='s')
bottom_most.pack(side="bottom",fill="x")


pic=tkinter.PhotoImage(file='karaoke.png')
Labelpic=tkinter.Label(top_frame,image=pic,bg="yellow",fg="blue")
Labelpic.grid(row=0)


length_track=tkinter.Label(top_frame,text="Length of the track: "+"--:--:--",bg='lightgreen')
length_track.grid(row=1)


current_timerf=tkinter.Label(top_frame,text=" Current: "+"--:--:--",bg="yellow")
current_timerf.grid(row=2)



def playpause_song():
    global p
    global b
    global h
    global a
    global fin
    global thready
    global file_name
    global new_file_name
    global ini
    global new_index
    global threadlist

    if p=='0':
        try: 
            file_name=playlist.curselection()
            file_name=int(file_name[0])
            ini=file_name
            file_name=playlist_list[file_name]     
            p='1'
            if mixer.music.get_busy():
                    mixer.music.stop()
                    time.sleep(1)
            else:
                time.sleep(1)          
            mixer.music.load(file_name)           
            mixer.music.play()
            new_index=-5
            playpause_button['image']=pause
            ext=os.path.basename(file_name)
            ext=ext.split(".")
            ext=ext[-1]
            if ext=='mp3':
                try: 
                    b=MP3(file_name)
                    a=b.info.length
                except:
                    length_track['text']="unable to find the length"
            elif ext=='wav' or 'ogg' :    
                try:
                    b=mixer.Sound(file_name)
                    a=b.get_length()
                except:
                    length_track['text']="unable to find the length"
            thready=threading.Thread(target=current_timef,args=(a,),daemon='True')
            threadlist.append(thready)   
            thready.start()  
            h=int(a/3600)
            if int(h/10)==0:
                length_track['text']="Length of the track: "+f"0{h}:"
            else:
                length_track['text']="Length of the track: "f"{h}:"
            a=a-(h*3600)
            h=int(a/60)
            if int(h/10)==0:
                length_track['text']=length_track['text']+f"0{h}:"
            else:
                length_track['text']=length_track['text']+f"{h}:"
            a=a-(h*60)
            h=int(a)
            if int(h/10)==0:
                length_track['text']=length_track['text']+f"0{h}:"
            else:
                length_track['text']=length_track['text']+f"{h}"            
        except:
            tkinter.messagebox.showerror("error","error in opening the file")
    elif p=='1':
        try:
            fin=playlist.curselection()
            fin=int(fin[0])
            if fin!=ini:
                p='0'
                mixer.music.stop()
                time.sleep(1)
                playpause_song()
            else:
                p='2'
                mixer.music.pause()
                playpause_button['image']=play
        except:
            tkinter.messagebox.showerror("error","error in opening the file")
    #p=1 and p=2 keeps on interchanging to play or pause the music
    elif p=='2':
        try:
            fin=playlist.curselection()
            fin=int(fin[0])
            if (fin!=ini):
                p='0'
                mixer.music.stop()
                time.sleep(1)
                playpause_song()

            else:
                p='1'
                mixer.music.unpause()
                playpause_button['image']=pause
        except:
            tkinter.messagebox.showerror("error","imwerror in opening the file")


def for_ward():
    try:
        global index
        global new_file_name
        global p
        global new_index
        global file_name
        new_index=playlist.curselection()
        new_index=int(new_index[0])
        if new_index < index-1:
            new_index+=1
            p='0'
            new_file_name=playlist_list[new_index]

            file_name=new_file_name
            playlist.selection_clear(new_index-1)
            playlist.selection_set(new_index)
            mixer.music.stop()
            time.sleep(1)
            playpause_song()
    except:
        playpause_song()
        tkinter.messagebox.showerror("Error","Error")

def back_ward():
    try:
        global index
        global new_file_name
        global p
        global file_name
        global new_index
        new_index=playlist.curselection()
        ##print(playlist.curselection())
        new_index=int(new_index[0])
        if new_index >0:
            new_index-=1
            
            p='0'
            new_file_name=playlist_list[new_index]
            file_name=new_file_name
            playlist.selection_clear(new_index+1)
            playlist.selection_set(new_index)
            mixer.music.stop()
            time.sleep(1)
            
            playpause_song()
    except:
        tkinter.messagebox.showerror("Error","Error")


backward_i=tkinter.PhotoImage(file="backward.png")
backward_button=ttk.tkinter.Button(mid_frame,image=backward_i,command=back_ward)
backward_button.grid(row=0,column=0,padx=10) 


play=tkinter.PhotoImage(file='play.png')
pause=tkinter.PhotoImage(file='pause.png')
playpause_button=ttk.tkinter.Button(mid_frame,image=play,command=playpause_song)
playpause_button.grid(row=0,column=1)


forward_i=tkinter.PhotoImage(file="forward.png")
forward_button=ttk.tkinter.Button(mid_frame,image=forward_i,command=for_ward)
forward_button.grid(row=0,column=2,padx=10)


def current_timef(timer):
    global p
    t=0
    mini=0
    seci=0
    houri=0
    while mixer.music.get_busy():
        if p=='1':
            k=t
            houri=int(t/3600)
            t=t-(houri*3600)
            mini=int(t/60)
            t=t-(mini*60)
            seci=int(t)
            t=t-(seci)
            t=k
            if houri < 10:
                houri="0"+str(houri)
            elif houri >10:
                houri=str(houri)
            if mini<10:
                mini="0"+str(mini)
            elif mini >10:
                mini=str(mini)
            if seci<10:
                seci="0"+str(seci)
            elif seci >10:
                seci=str(seci)
            current_timerf['text']="current : "+str(houri)+":"+str(mini)+":"+str(seci)
            time.sleep(1)         
            t+=1


def vol_music(vol):
    volume=int(vol)/100
    mixer.music.set_volume(volume)


vol_level=tkinter.Scale(bot_frame,from_=0,to_=100,orient='horizontal' ,command=vol_music)
vol_level.set(75)
vol_music(75)
vol_level.grid(row=1)


def mute_unmute():
    global q
    global vol
    if p=='0':
        tkinter.messagebox.showerror("Error","No music found")
    elif p=='2':
        tkinter.messagebox.showerror("error","Music is paused")
    elif p=='1' and q=='0':
        try:
            q='1'
            vol_music(0)
            vol_level.set(0)
            muteunmute_button['image']=unmute
        except:
            tkinter.messagebox.showerror("Error","Error")
    elif p=='1' and q=='1':
        try:
            q='0'
            vol_music(f'{vol}')
            vol_level.set(f'{vol}')
            muteunmute_button['image']=mute
        except:
            tkinter.messagebox.showerror("Error","Error")


mute=tkinter.PhotoImage(file='mute.png')
unmute=tkinter.PhotoImage(file='unmute.png')
muteunmute_button=ttk.tkinter.Button(bot_frame,image=mute,command=mute_unmute)
muteunmute_button.grid(row=0,column=1)


def rewind_music():
    global p
    if p=='0':
        tkinter.messagebox.showerror("Error","No music found")
    elif p=='2':
        try:
            p='0'
            mixer.music.stop()
            time.sleep(2)
            playpause_song()
        except:
            tkinter.messagebox.showerror("Error","Error") 
    elif p=='1':
        try:
            mixer.music.stop()
            time.sleep(2)
            p='0'
            playpause_song()
        except:
            tkinter.messagebox.showerror("Error","Error") 


   
rewind=tkinter.PhotoImage(file='rewind.png')
rewind_button=ttk.tkinter.Button(bot_frame,image=rewind,command=rewind_music)
rewind_button.grid(row=0,column=0)


def click_cross():
    window.destroy()


window.protocol("WM_DELETE_WINDOW",click_cross)


window.mainloop()
