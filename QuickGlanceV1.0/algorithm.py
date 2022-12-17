#%% Importing libraries
import os
import random
import tkinter
import time
#%% Graphic User interphase definition
window = tkinter.Tk()
# This places the main window on top of other programs
window.attributes('-topmost',True)
window.geometry("700x100")
window.title("QuickGlance")
window.configure(bg='#DDE4EA')
# Time variable (ms)
time_delay = 3000

# OOP algorithm
class base:
    #Variables
    def __init__(self, fileObject):
        self.__fileObject = fileObject.readlines()
        self.__lines = 0
        self.__randomList = []
        self.__lineDisplayed = []
        self.MainLabel = tkinter.Label(window, 
        text = "This is a test",
        bg = '#EAC950',
        font=("Helvetica", 20),
        #fg = '#EAC950' This sets font color
        )
        self.MainLabel.pack(side="top")  

    def update_label(self,x=0):
        #Stop condition
        if x < self.lines:
            self.MainLabel.config(text = self.lineDisplayed[x])
            x+=1
        else: x=0
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
fileObjectX = open(fileName, 'r')
Main_object = base(fileObjectX)

# Counts the amount of lines in the file
Main_object.counter()
# Generates random numbers list 
Main_object.randomList()
# Displays random lines
Main_object.displayLine()
#This function changes the label phrase
window.after(time_delay, lambda: Main_object.update_label())
# Testing
print(Main_object.lineDisplayed)
#%%
window.mainloop()   
# %%
