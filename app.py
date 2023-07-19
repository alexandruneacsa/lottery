from tkinter import *
from tkinter import ttk
from functools import partial
from functools import *
import random
import pyglet
import threading
import time
import winsound

class PickingNumbers():

    def __init__(self):
        self.picketNumbers = []

    def run(self):
        self.main = Tk()
        self.main.title("Multiple choice listbox")
        self.main.geometry("+650+50")
        self.main.resizable(width=10,height=10)

        self.frame = ttk.Frame(self.main)
        self.frame.grid(column=11,row=11)

        rand = 1
        y = 0
        for i in range(1,50):
            print(i)
            y += 1
            if i%10 == 1:
                rand += 1
                y = 0
            
            self.label = Label(self.main, text=str(i),background='black',foreground='white')
            self.label.config(font = ('Arial',14) )
            self.label.grid(row=rand, column=y, padx=5, pady=5)
            self.label.bind("<Enter>", partial(self.color_config, self.label, "blue"))
            self.label.bind("<Leave>", partial(self.color_config, self.label, "white"))
            self.label.bind("<Button-1>", lambda event,number = i:self.callback(event, number) )

            btn = ttk.Button(self.frame, text= "Pick 6 numbers",command=self.DisplayNumbers )
            btn.grid(column=10, row=10)

        self.main.mainloop()

    def color_config(self, widget, color, event):
        widget.configure(foreground=color)

    def callback(self, event, n):
        print(event,n)
        event.widget.config(background='blue')
        self.picketNumbers.append(n)

    def PlayVideo(self):
        videos = ['videos/2.mp4']
        self.vid_path = random.choice(videos)
        print(self.vid_path)

        window = pyglet.window.Window(width=810, height= 500)
        x,y = window.get_location()
        print(x,y)
        window.set_location(x+400, y+100)

        player = pyglet.media.Player()
        source = pyglet.media.StreamingSource()
        mediaLoad = pyglet.media.load(self.vid_path)
        player.queue(mediaLoad)
        player.play()

        @window.event
        def on_draw():
            if player.source and player.source.video_format:
                player.get_texture().blit(10,10)
        
        pyglet.app.run()

    def DisplayNumbers(self):

        t = threading.Thread(target = self.GettingResult)
        t.start()
        self.main.destroy()

        self.main2 = Tk()
        self.main2.title("your picked numbers")
        self.main2.geometry('400x50+10+10')
        self.label1 = Label(self.main2, text=str(self.picketNumbers),background='black',foreground='white')
        self.label1.config(font = ('Arial',14) )
        self.label1.grid(row=10, column=11, padx=5, pady=5)
        self.main2.mainloop()

    def GettingResult(self):
        print("Extracting numbers")
        self.PlayVideo()
        t = threading.Thread(target = self.PlayVideo )
        t.start()
        time.sleep(80) #wait 1m33s
        pyglet.app.exit()
        
        self.list1 =[]
        if self.vid_path ==  'videos/1.mp4':
            self.list1.append(["9","10","19","29","5","8"])
        elif self.vid_path == "videos/2.mp4":
            self.list1.extend(["6","12","17","13","22","7"])
        elif self.vid_path == "videos/3.mp4":
            self.list1.extend(["31","34","35","29","41","8"])

        self.main3 = Tk()
        self.main3.title("lottery winners numbers")
        self.main3.geometry("400x50+10+80")
        self.label4 = Label(self.main3, text=str(self.list1), background='green', foreground='white')
        self.label4.config(font = ('Arial',14))
        self.label4.grid(row=10, column=11, padx=5, pady=5)
        time.sleep(1)

        t2 = threading.Thread(target = self.Compare)
        t2.start()

        self.label4.mainloop()

    def Compare(self):

        winners_count = 0
        for i in self.list1:
            for j in self.picketNumbers:
                if int(i) == int(j):
                    winners_count += 1
        
        print("Contor", winners_count)

        self.main4 = Tk()
        if winners_count == 0 or winners_count == 1 or winners_count == 2:
            self.main4.title("Better luck next time!")
            self.main4.geometry("400x250+600+300")
            self.label5 = Label(self.main4, text= "Try again!", background='red', foreground='white')
            self.label5.config(font = ('Arial',14))
            self.label5.grid(row=10, column=11, padx=5, pady=5)
        elif winners_count == 3 or winners_count == 4 or winners_count == 5 or winners_count == 6:
            winsound.PlaySound("./notification.wav",winsound.SND_FILENAME)
            self.main4.title("Congratulation we have a winner")
            self.main4.geometry("700x250+600+300")

            self.label5 = Label(self.main4, text= "You had matched! ("+str(winners_count)+ ") numbers", background='green', foreground='white')
            self.label5.config(font = ('Arial',14))
            self.label5.grid(row=15, column=10, padx=5, pady=5)

            self.label6 = Label(self.main4, text= "Your numbers! "+str(self.picketNumbers), background='green', foreground='white')
            self.label6.config(font = ('Arial',14))
            self.label6.grid(row=17, column=10, padx=5, pady=5)

            self.label7 = Label(self.main4, text= "Winners numbers! "+str(self.list1), background='green', foreground='white')
            self.label7.config(font = ('Arial',14))
            self.label7.grid(row=20, column=10, padx=5, pady=5)

        tt = threading.Thread(target=self.Destroying)
        tt.start()    

        tt1 = threading.Thread(target=self.Destroying2)
        tt1.start()  

        self.main4.mainloop()
    
    def Destroying(self):
        self.main2.destroy()

    def Destroying2(self):
        self.main3.destroy()

pk = PickingNumbers()
pk.run()





            
            

                






