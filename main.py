from tkinter import *
import pygame
from PIL import Image,ImageTk
import os

class player(Tk):
    ''' this class contains all the main functions of a music player app'''
    _initial_volume = 0.2
    _pause_count = 0
    _font_style = ("Helvetica",12,"bold")
    def __init__(self,parent):
        self.parent = parent
        self.parent.title("Music Player")
        self.parent.geometry("350x520")
        self.parent.minsize(350,520)
        self.parent.maxsize(350,520)
        self.parent.iconbitmap("music-icons/Iynque-Ios7-Style-Music.ico")
        
        # before calling any methods let us initialize the pygame and its mixer module
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        pygame.mixer.music.set_volume(self._initial_volume)
        # calling class method to make ui of the app
        self.playMenuButton()

    def play_clicked(self):
        print("Play Button is Clicked!!")
        song = self.playList.get(ACTIVE)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(1)
    
    def pause_clicked(self):
        print("Pause Button is Clicked!!")
        self._pause_count+=1
        if self._pause_count%2!=0:
            pygame.mixer.music.pause()
            print("music has been paused!!")
        else:
            pygame.mixer.music.unpause()
            print("music has resumed!")

    def volume_up(self):
        print("Volume Increased by 10%")
        self._initial_volume += 0.1
        pygame.mixer.music.set_volume(self._initial_volume) 

    def volume_down(self):
        print("Volume Decreased by 10%")
        self._initial_volume -= 0.1
        pygame.mixer.music.set_volume(self._initial_volume)

    def about_info(self):
            new_root = Tk()
            new_root.minsize(350,350)
            new_root.maxsize(350,350)
            new_root.title("About and Credits")
            new_root.iconbitmap("C:/Users/sandarbh/Desktop/currentProjects/python/pythonProjects/for-practice/music-player-app/music-icons/Hopstarter-Button-Button-Info.ico")

            s = Scrollbar(new_root)
            t = Text(new_root,width=350,height=350,background="white",foreground="red",font=self._font_style)
            s.pack(side=RIGHT,fill=Y)
            t.pack(side=LEFT,fill=X)
            s.config(command=YView)
            t.config(yscrollcommand = s.set)
            quote = '''\nProject name: Music Player for fun \nCreated by: Sandarbh Tiwari \nPurpose: For educational and practice purpose
            \nCredits for successful completion \n\n1. Iconset: Button Icons by Hopstarter (17 icons)\nArtist: Hopstarter (Jojo Mendoza) (Available for custom work)\nLicense: CC Attribution-Noncommercial-No Derivate 4.0\nCommercial usage: Allowed (Author Arrangement required -> Visit artist website for details)\n\n2. Music Icon\nArtist: iynque\nIconset: iOS7 Style Icons (69 icons)\nLicense: CC Attribution-Noncommercial-No Derivate 4.0\nCommercial usage: Not allowed\nReadme file: Description.txt\n\n3. Button Info Icon\nArtist: Hopstarter (Available for custom work)\nIconset: Button Icons (17 icons)\nLicense: CC Attribution-Noncommercial-No Derivate 4.0\nCommercial usage: Allowed (Author Arrangement required -> Visit artist website for details).''' 
            t.insert(END,quote)
            new_root.mainloop()

    def playMenuButton(self):
        ''' this function creates all the basic buttons of an music player app'''
        def getfiles():
            songFiles = []
            print("Your Current Working Directory is: "+str(os.getcwd()))
            # chnaging directory to access music files
            directory = os.chdir("C:/Users/sandarbh/Desktop/currentProjects/python/pythonProjects/to-github/music-player-app/files")
            # storing all the music files in a list
            for file in os.listdir(directory):
                if file.endswith('.mp3') or file.endswith('.ogg') or file.endswith('.wav'):
                    songFiles.append(file)
                else:
                    print("Not a music file!")
            return(songFiles)
        
        
        # welcome label
        self.label = Label(self.parent,text="Welcome, Let's Play Music",padx=15,pady=15,font=("Helvetica",15,"bold"),background="yellow")
        self.label.pack()
        # play-button
        btnPlayImage = Image.open("music-icons/Button-Play-icon.png")
        render_play = ImageTk.PhotoImage(btnPlayImage)
        self.btn_play = Button(self.parent,image=render_play,padx=5,pady=5,width=40,height=40,command=self.play_clicked)
        self.btn_play.image = render_play
        
        # pause-button
        btnPauseImage = Image.open("music-icons/Button-Pause-icon.png")
        render_pause = ImageTk.PhotoImage(btnPauseImage)
        self.btn_pause = Button(self.parent,image=render_pause,padx=5,pady=5,width=40,height=40,command=self.pause_clicked)
        self.btn_pause.image = render_pause
        
        # creating a volume up button
        btnVolUp = Image.open("music-icons/Button-Add-icon.png")
        render_Vol_up = ImageTk.PhotoImage(btnVolUp)
        self.btnVolumeUp = Button(self.parent,image=render_Vol_up,padx=5,pady=5,width=40,height=40,command=self.volume_up)
        self.btnVolumeUp.image = render_Vol_up
        
        # creating a volume up button
        btnVolDown = Image.open("music-icons/Button-Delete-icon.png")
        render_Vol_down = ImageTk.PhotoImage(btnVolDown)
        self.btnVolumeDown = Button(self.parent,image=render_Vol_down,padx=5,pady=5,width=40,height=40,command=self.volume_down)
        self.btnVolumeDown.image = render_Vol_down
        
        # creating an credits and about button
        btnAbout = Image.open("music-icons/Button-Info-icon.png")
        render_btnAbout = ImageTk.PhotoImage(btnAbout)
        self.about_btn = Button(self.parent,text="About",font=self._font_style,image=render_btnAbout,padx=5,pady=5,width=80,height=35,compound=LEFT,command=self.about_info)
        self.about_btn.image = render_btnAbout

        # creating a list-box gui
        songsList = getfiles()
        self.playList = Listbox(self.parent,font=("Helvetica",12),highlightcolor="pink",selectmode=SINGLE,background="pink")
        self.playList.config(width=50,height=12)
        for items in songsList:
            pos = 0
            self.playList.insert(pos,items)
            pos = pos+1
        
        # create a label for now playing music
        self.play_label = Label(self.parent,text="Play",font=self._font_style,foreground="blue")
        self.pause_label = Label(self.parent,text="Pause/Unpause",font=self._font_style,foreground="blue")
        self.volume_up_label = Label(self.parent,text="Volume Up",font=self._font_style,foreground="blue")
        self.volume_down_label = Label(self.parent,text="Volume Down",font=self._font_style,foreground="blue")
        
        # creating a packing order of all the widgets
        self.playList.pack()
        self.btn_play.place(x=80,y=300)
        self.play_label.place(x=83,y=350)
        self.btn_pause.place(x=240,y=300)
        self.pause_label.place(x=200,y=350)
        self.btnVolumeUp.place(x=80,y=390)
        self.volume_up_label.place(x=60,y=440)
        self.btnVolumeDown.place(x=240,y=390)
        self.volume_down_label.place(x=205,y=440)
        self.about_btn.pack(side=BOTTOM)

if __name__ == '__main__':
    root = Tk()
    runPlayer = player(root)
    root.mainloop()