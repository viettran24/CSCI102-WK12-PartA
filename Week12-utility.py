#Viet Tran
#Section B
#Week 12 - Part A
import re
import string

def PrintOutput(string):
    print("OUTPUT:", string)

def LoadFile(filename):
    with open(filename) as file:
        elementList = []
        for line in file:
            elementList.append(line)
    return elementList

def UpdateString(string1,string2,index):
    letterList = []
    for char in string1:
        letterList.append(char)
    letterList[index] = string2
    return letterList

def FindWordCount(filename,string):
    my_list = LoadFile(filename)
    my_string = ''
    for x in my_list:
        my_string += x
    my_string = my_string.count(string)
    return my_string
PrintOutput(FindWordCount("README.md","Viet"))
