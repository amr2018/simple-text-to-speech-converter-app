
import pyttsx3
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import threading
import time
import os

class app:
    def __init__(self):

        self.window = Tk()
        self.text = ''
        self.type = 1
        self.save_file = os.getcwd()

        

        self.window.geometry('400x360')
        self.window.title('TEXT TO SPEECH APP')

        #make label for app
        self.label = Label(
        self.window, 
        text="TEXT TO SPEECH APP", 
        font = ('san-serf', 20), 
        fg="#ff7675")
        self.label.place(x=10, y=10)

        #the text place
        self.text_input = Text(
            self.window, 
            font = ('san-serf', 12), 
            bd=0, 
            height = 10, 
            width = 42)

        self.text_input.place(x=10, y=55)

        self.rate = 125
        self.volume = 0.5

        self.sound_type = StringVar(self.window)
        self.sound_type.set("Female") # default value

        #to set type of sound

        self.s_type = OptionMenu(self.window, self.sound_type,
         "Male", "Female", command=self.change_type)

        self.s_type.config(bd=0, bg="#ff6b6b", fg="white", 
        font = ('san-serf', 12), height= 2)

        self.s_type.place(x=230, y=240)

        
    
        #volume
        self.vol = Scale(
            self.window,
            label = "volume", 
            bd=0,
            bg = "white",
            from_ = 0.3,
            to = 1,
            orient = HORIZONTAL ,
            resolution = .1,
            ####################
            command=self.change_vol
            ####################
        ).place(x=10, y=240)


        self.rt = Scale(
            self.window,
            label = "speed", 
            bd=0,
            bg = "white",
            from_ = 100,
            to = 500,
            orient = HORIZONTAL ,
            resolution = 1,
            ####################
            command=self.change_rate
            ####################
        ).place(x=120, y=240)

        


        #text to speech button
        self.btn = Button(
            self.window, text="speech", 
            bd=0, font = ('san-serf', 12), 
            fg="white", bg="#ff7675", height = 2, 
            width = 10, command=self.textToSpeech)

        self.btn.place(x=10, y=300)

        #delet text
        self.delbtn = Button(self.window, text="delete text", 
        bd=0, font = ('san-serf', 12), 
        fg="white", bg="red", height = 2, 
        width = 10, command=self.delete_text)

        self.delbtn.place(x=120, y=300)

        #save to file
        self.delbtn = Button(self.window, text="save", 
        bd=0, font = ('san-serf', 12), 
        fg="white", bg="#3498db", height = 2, 
        width = 10, command=self.Save_to_file)


        self.delbtn.place(x=230, y=300)


        self.window.mainloop()

    
    def change_type(self, v):

        if v == 'Male':
            self.type = 0
            self.s_type.config(bg="#341f97")
        else:
            self.type = 1
            self.s_type.config(bg="#ff6b6b")

    

    def change_rate(self, value):
        self.rate = int(value)

    def change_vol(self, value):
        self.volume = float(value)
    
    def textToSpeech(self):
        self.text = self.text_input.get("1.0",END)

        def sppech():
            try:
                if len(self.text) > 1:
                    time.sleep(1)
                    engine = pyttsx3.init()
                    voices = engine.getProperty('voices')[self.type]
                    engine.setProperty('voice', voices.id)
                    rate = engine.getProperty('rate')
                    engine.setProperty('rate', self.rate)
                    volume = engine.getProperty('volume')
                    engine.setProperty('volume', self.volume)
                    engine.say(self.text)
                    engine.runAndWait()
                else:
                    messagebox.showinfo('info','please enter any text to speech')
            except Exception as e:
                messagebox.showerror(':(', e)
        
        
        try:
            threading.Thread(target=sppech).start()
        except Exception as e:
            messagebox.showerror(':(', e)
           
    
    def delete_text(self):
        self.text_input.delete("1.0","end")
        self.text = self.text_input
    
    def Save_to_file(self):

        def save():
            self.text = self.text_input.get("1.0",END)
            try:
                if len(self.text) > 1:
                    date_time = datetime.now().strftime("%m_%d_%Y_%H-%M-%S")
                    
                    engine = pyttsx3.init('sapi5')
                    voices = engine.getProperty('voices')[self.type]
                    engine.setProperty('voice', voices.id)
                    rate = engine.getProperty('rate')
                    engine.setProperty('rate', self.rate)
                    volume = engine.getProperty('volume')
                    engine.setProperty('volume', self.volume)
                    engine.save_to_file(self.text.strip(), self.save_file+ '/'+ date_time +'.mp3')
                    
                    engine.runAndWait()
                else:
                    messagebox.showinfo('info','please enter any text to save speech')
            except Exception as e:
                messagebox.showerror(':(', e)
            
        
        threading.Thread(target=save).start()

myapp = app()
