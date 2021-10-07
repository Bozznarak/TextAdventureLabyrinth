import time 
import os
import sys
from decimal import Decimal as D
# import generatePlayground
# import visualisationLab 
import createPaths
import createPlayground

# currentLocation = 2.2
gameState = True
currentOptions = ["Test"]

labyrinthDict =    {1.1: ["wallNorth", "wallEast", "wallWest"],1.2:["wallNorth","wallEast", "wallWest"],1.3:["wallWest"],
                    2.1:["wallWest"],2.2:["start", "wallEast", "wallSouth", "actionLook;at;watch", "actionLeave;a;mark"],2.3:["wallWest"],
                    3.1:["wallSouth", "wallWest"],3.2:["wallNorth", "wallSouth"],3.3:["finish"]}
directionDict = {"North": -1, "East": 0.1, "South": 1, "West": -0.1}

markingsDict = {1.1:"",1.2:"",1.3:"",
                2.1:"", 2.2:"May this piece of chalk help you navigate this maze...", 2.3:"",
                3.1:"", 3.2:"", 3.3:""}

markingsDictTemplate = {1.1:"",1.2:"",1.3:"",
                        2.1:"", 2.2:"", 2.3:"",
                        3.1:"", 3.2:"", 3.3:""}

def leaveMark():
    mark = str(input("use chalk to scribble on the floor (user input required): "))
    markingsDict[playerTest.position] = mark
def readMark():
    if markingsDict[playerTest.position] != "":
        print(markingsDict[playerTest.position])
    else:
        print("there are no chalk markings")



def wallListString(wallList):
    if len(wallList)>1:
        varWall = "There are walls to the "
    else:
        varWall = "There is a wall to the "
    wallString = f"{varWall}"
    for wall in range(0,len(wallList)):
        wallString += f"{wallList[wall][4:]} & "
    wallString += "\b\b."
    return wallString

def filterOptions(currentLocationData):
    global currentOptions 
    filterList =  ["wallNorth", "wallEast", "wallSouth", "wallWest"]
    for option in currentLocationData:
        if option in filterList:
            filterList.remove(option)
    for i in range(0,len(filterList)):
        filterList[i] = filterList[i][4:]
    optionsLeft= f"You could walk"
    for option in filterList:
        optionsLeft += f" {option.upper()} or"
    optionsLeft += f"\b\b..."
    currentOptions = filterList
    return optionsLeft

def presentActions():
    actionString = ""
    for key in actionDict.keys():
        actionString += key + ", "
    actionString += "\b\b."
    return actionString

def presentOptions(location):
    global gameState
    global labyrinthDict
    # global currentLocation
    listWalls = []
    listActions = []
    locationData = labyrinthDict[round(location, 3)]
    for info in locationData:
        if "finish" in info:
            gameState = False
            break
        if "wall" in info:
            listWalls.append(info)
        if "action" in info:
            listActions.append(info)
    if gameState:
        print(wallListString(listWalls))
        print(filterOptions(listWalls), end=" ")
        print(f"you could also type: {presentActions()}")

def getValueFromDict(key, dict):
    value = dict[key]
    value = round(value, 2)
    return value

def checkInput(userInput):
    if userInput != "":
        inputCapitalized = userInput[0].upper() + userInput[1:]
        if inputCapitalized in currentOptions:
            moveTo(inputCapitalized)
        elif inputCapitalized in actionDict:
                actionDict[inputCapitalized]()
        else:
            print("please choose a valid option")
            print(f"valid options are: {currentOptions}")
            userInput = input()
            checkInput(userInput)
    else:
        print("please choose a valid option")
        print(f"valid options are: {currentOptions}")
        userInput = input()
        checkInput(userInput)
def moveTo(direction):
    playerTest.position += getValueFromDict(direction, directionDict)
    labyrinthDict2[round(playerTest.position, 2)].visited = True
    presentOptions(playerTest.position)



class player:
    def __init__(self, name="", position=1.1, items=[], options=[], mapUsed=False):
        self.name = name
        self.position = position
        self.items = items
        self.options = options
        self.mapUsed = mapUsed

class Tile:
    def __init__(self, position=0.0, visited=False, start=False, finish=False ,mapCharacter=chr(9634), walls=[]):
        self.position = position
        self.visited = visited
        self.start = start
        self.finish = finish
        self.mapCharacter = mapCharacter
        self.walls = walls

def showMap():
    counter = 2
    roomList = []
    roomsPerLine = []
    for key in labyrinthDict2:
        # print(labyrinthDict2[key].mapCharacter)
        if (key/counter) > 1.0:
            print("\n")
            counter += 1
            roomList.append(roomsPerLine)
            roomsPerLine = []
        if labyrinthDict2[key].start:
            print(f" {key} : X ",end="")
        elif labyrinthDict2[key].finish:
            print(f" {key} : Y ",end="")
        elif labyrinthDict2[key].visited:
            print(f" {key} : {labyrinthDict2[key].mapCharacter} ",end="")
        else:
            print(f" {key} : {chr(9634)} ",end="")
        roomsPerLine.append(key)
    roomList.append(roomsPerLine)
    if not playerTest.mapUsed:
        print("\nAt the bottom is a note: X Marks your start, Y is where you need to go")
        playerTest.mapUsed = True

actionDict = {"Chalk": leaveMark, "Read": readMark, "Map": showMap}

varTestLap = createPaths.generatePaths()
playerStart = createPaths.fixedStartCorr
playerFinish = createPaths.finishCorridorVis
os.system("cls")
charIdentDict = {"W": chr(9568), "S":chr(9577), "SW": chr(9562), "E": chr(9571),"EW": chr(9553), "ES":chr(9565), "ESW": chr(9576), "N": chr(9574), "NW":chr(9556),"NS": chr(9552), "NSW":chr(9566),"NE": chr(9559), "NEW":chr(9573),"NES":chr(9569), "NESW":chr(9634), "":chr(9580)}
labyrinthDict.clear()
labyrinthDict2 = {}
print(varTestLap)
boolToStringDirectionDict = {0 : "wallNorth", 1: "wallEast", 2: "wallSouth", 3: "wallWest"}
for key in varTestLap:
    newTile = Tile(walls=[])
    newValues = []
    if key == playerStart:
        newValues.append("start")
        newTile.start = True
    if key == playerFinish:
        newValues.append("finish")
        newTile.finish = True
    charKey = ""
    for i in range(0,4):
        if varTestLap[key][i]:
            charKey += boolToStringDirectionDict[i][4:5]
            newValues.append(boolToStringDirectionDict[i])
            newTile.walls.append(boolToStringDirectionDict[i])
    newValues.append(charKey)
    newTile.mapCharacter = charIdentDict[charKey]
    print(charKey)
    newTile.position = key
    labyrinthDict[key] = newValues
    labyrinthDict2[key] = newTile
    print(vars(newTile))
    newTile.walls = []




print(f"starting pos: {labyrinthDict[playerStart]}, tile: {playerStart}")
print(f"finish pos: {labyrinthDict[playerFinish]}, tile: {playerFinish}")

# print(roomList)


# testDict = labyrinthDict
# testDict.clear()
# print(testDict)



print(labyrinthDict2[1.2].position)
print(labyrinthDict2[1.1].position)
introText = "You wake up at a crossing in, what seems to be, a labyrinth. Torches illuminate these corridors..."
introText2 ="As you get up on your feet you notice a pieces of chalk on the ground and a message written on the wall:\nUse the chalk to leave notes, may theses assist you in finding a way out..."
print(introText)
print(introText2)
playerTest = player("testPlayerName", playerStart, [], [])
presentOptions(playerTest.position)
while gameState:
    userInput = input()
    checkInput(userInput)
print("As you turn the next corner, the last thing you see is a minotaur charging at you .....\nHanding you a gratulation card: YOU MADE IT !!!!!  *WUHUUUUU*")
