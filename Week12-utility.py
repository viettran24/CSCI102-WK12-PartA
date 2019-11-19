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

players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
scores = [5, 8, 10, 6, 10, 4]
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]

def ScoreFinder(players,scores,name):
    i = 0
    clean_list = []
    for x in players:
        clean_list.append(x.lower())
        if x != name:
            i = i + 1
        else:
            return players[i], "has a score of", scores[i]
    if name not in players:
        return "player not found"


def Union(list1,list2):
    new_list = []
    for x in list1:
        new_list.append(x)
    for x in list2:
        new_list.append(x)
    return new_list

def Intersection(firstlist,secondlist):
    combined_list = Union(firstlist,secondlist)
    clean_list = []
    no_dupes = []
    for x in combined_list:
        if combined_list.count(x) >= 2:
            clean_list.append(x)
    for x in clean_list:
        if x not in no_dupes:
            no_dupes.append(x)
    return no_dupes

PrintOutput(Intersection(players,players2))


