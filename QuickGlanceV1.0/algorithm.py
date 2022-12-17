#%% Importing libraries
import os
import random
#%%
class base:
    #Variables
    def __init__(self, fileObject):
        self.__fileObject = fileObject.readlines()
        self.__lines = 0
        self.__randomList = []
        self.__lineDisplayed = []
        
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

# Testing
print(Main_object.lines)
print(Main_object.randomList)
print(Main_object.lineDisplayed)
 
    
# %%
