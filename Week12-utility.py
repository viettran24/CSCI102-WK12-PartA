#Viet Tran
#Section B
#Week 12 - Part A

def PrintOutput(string):
    print("OUTPUT:", string)

def LoadFile(filename):
    with open(filename) as file:
        elementList = []
        for line in file:
            elementList.append(line)
    return elementList
    

