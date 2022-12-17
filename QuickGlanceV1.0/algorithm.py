#%% Importing libraries
import os
import random
import tkinter
from tkinter import *

#%% Graphic User interphase definition
window = tkinter.Tk()

#This function allows us to use py-to-exe program to generate a onefile program
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


#%% This places the main window on top of other programs
window.attributes('-topmost',True)
window.attributes('-alpha',0.85)
window.geometry("700x80")
window.title("QuickGlance V1.0")
window.configure(bg='#DDE4EA')
path = resource_path('image.ico')
window.iconbitmap(path)
# OOP algorithm
class base:
    #Variables
    def __init__(self, fileObject):
        self.__fileObject = fileObject.readlines()
        self.__lines = 0
        self.__randomList = []
        self.__lineDisplayed = []

        self.MainLabel = tkinter.Label(window, 
            text = "Enjoy your study session",
            bg = '#EAC950',
            font=("Helvetica", 14),)
        self.MainLabel.pack(side="top")  

        self.bar = tkinter.Scale(window,
            from_=5,
            resolution=5,
            to=30,
            orient='horizontal',
            bg = '#E36476')
        self.bar.pack(side="top") 
        #self.bar.grid(row = 2, column = 1)
        

    def update_label(self,x=0):
        #Stop condition
        if x < self.lines:
            self.MainLabel.config(text = self.lineDisplayed[x])
            user_delay = self.bar.get()
            time_delay = 1000*user_delay
            x+=1
            # Updates x value at the end of the list is displayed
            if x<self.lines:
                pass
            else:
                x = 0
        window.after(time_delay, lambda: self.update_label(x))

    #__fileObject getter 
    @property
    def fileObject(self):
        return self.__fileObject
    #__lines getter & setter
    @property
    def lines(self):
        return self.__lines
    @lines.setter
    def lines(self, new_line):
        self.__lines = new_line  
        
    #__randomList getter & setter
    @property
    def randomList(self):
        return self.__randomList
    @randomList.setter
    def randomList(self, new_randomList):
        self.__randomList = new_randomList
        
    #__lineDisplayed getter & setter
    @property
    def lineDisplayed(self):
        return self.__lineDisplayed
    @lineDisplayed.setter
    def lineDisplayed(self, new_lineDisplayed):
        self.__lineDisplayed = new_lineDisplayed
    
    
    #Public methods for actions
    def counter(self):
        count = 0
        reading =  self.fileObject
        for n in reading:
            count += 1
        self.lines = count
            
    def randomList(self):
        numbers = random.sample(range(0, self.lines), self.lines)
        self.randomList = numbers

    def displayLine(self):
        output = []
        reading =  self.fileObject
        for n in self.randomList:
            output.append(reading[n].strip())
        self.lineDisplayed = output

################################################################

#%% File name to be read
fileName = 'file.txt'
fileObjectX = open(fileName, 'r', encoding="utf-8")
Main_object = base(fileObjectX)

# Counts the amount of lines in the file
Main_object.counter()
# Generates random numbers list 
Main_object.randomList()
# Displays random lines
Main_object.displayLine()
#This function changes the label phrase
Main_object.update_label()

# Testing
print(Main_object.lineDisplayed)




window.mainloop()   
# %%
