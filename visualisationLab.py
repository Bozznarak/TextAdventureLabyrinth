import random
import generatePlayground as GPG
# mit import Decimal kann man Rundungsprobleme aufheben und muss dann + decimal(0.01) rechnen

# playgroundDic, startCorridor, finishCorridor,xAxis,yAxis
playgroundDicVis, startCorridorVis, finishCorridorVis, xAxisVis, yAxisVis = GPG.createPlayground()
print(xAxisVis,"XAchse")
print(yAxisVis,"YAchse")
print(startCorridorVis)

# print(playgroundDicVis, startCorridorVis, finishCorridorVis, xAxisVis, yAxisVis)


# examples
# playgroundDicVis = {1.1: [True, True, True, True, False, 'position 1.1'], 1.2: [True, True, True, True, False, 'position 1.2'], 1.3: [True, True, True, True, False, 'position 1.3'], 1.4: [True, True, True, True, False, 'position 1.4'], 1.5: [True, True, True, True, False, 'position 1.5'], 1.6: [True, True, True, True, False, 'position 1.6'], 1.7: [True, True, True, True, False, 'position 1.7'], 1.8: [True, True, True, True, False, 'position 1.8'], 2.1: [True, True, True, True, False, 'position 2.1'], 2.2: [True, True, True, True, False, 'position 2.2'], 2.3: [True, True, True, True, False, 'position 2.3'], 2.4: [True, True, True, True, False, 'position 2.4'], 2.5: [True, True, True, True, False, 'position 2.5'], 2.6: [True, True, True, True, False, 'position 2.6'], 2.7: [True, True, True, True, False, 'position 2.7'], 2.8: [True, True, True, True, False, 'position 2.8'], 3.1: [True, True, True, True, False, 'position 3.1'], 3.2: [True, True, True, True, False, 'position 3.2'], 3.3: [True, True, True, True, False, 'position 3.3'], 3.4: [True, True, True, True, False, 'position 3.4'], 3.5: [True, True, True, True, False, 'position 3.5'], 3.6: [True, True, True, True, False, 'position 3.6'], 3.7: [True, True, True, True, False, 'position 3.7'], 3.8: [True, True, True, True, False, 'position 3.8'], 4.1: [True, True, True, True, False, 'position 4.1'], 4.2: [True, True, True, True, False, 'position 4.2'], 4.3: [True, True, True, True, False, 'position 4.3'], 4.4: [True, True, True, True, False, 'position 4.4'], 4.5: [True, True, True, True, False, 'position 4.5'], 4.6: [True, True, True, True, False, 'position 4.6'], 4.7: [True, True, True, True, False, 'position 4.7'], 4.8: [True, True, True, True, False, 'position 4.8'], 5.1: [True, True, True, True, False, 'position 5.1'], 5.2: [True, True, True, True, False, 'position 5.2'], 5.3: [True, True, True, True, False, 'position 5.3'], 5.4: [True, True, True, True, False, 'position 5.4'], 5.5: [True, True, True, True, False, 'position 5.5'], 5.6: [True, True, True, True, False, 'position 5.6'], 5.7: [True, True, True, True, False, 'position 5.7'], 5.8: [True, True, True, True, False, 'position 5.8'], 6.1: [True, True, True, True, False, 'position 6.1'], 6.2: [True, True, True, True, False, 'position 6.2'], 6.3: [True, True, True, True, False, 'position 6.3'], 6.4: [True, True, True, True, False, 'position 6.4'], 6.5: [True, True, True, True, False, 'position 6.5'], 6.6: [True, True, True, True, False, 'position 6.6'], 6.7: [True, True, True, True, False, 'position 6.7'], 6.8: [True, True, True, True, False, 'position 6.8'], 7.1: [True, True, True, True, False, 'position 7.1'], 7.2: [True, True, True, True, False, 'position 7.2'], 7.3: [True, True, True, True, False, 'position 7.3'], 7.4: [True, True, True, True, False, 'position 7.4'], 7.5: [True, True, True, True, False, 'position 7.5'], 7.6: [True, True, True, True, False, 'position 7.6'], 7.7: [True, True, True, True, False, 'position 7.7'], 7.8: [True, True, True, True, False, 'position 7.8'], 8.1: [True, True, True, True, False, 'position 8.1'], 8.2: [True, True, True, True, False, 'position 8.2'], 8.3: [True, True, True, True, False, 'position 8.3'], 8.4: [True, True, True, True, False, 'position 8.4'], 8.5: [True, True, True, True, False, 'position 8.5'], 8.6: [True, True, True, True, False, 'position 8.6'], 8.7: [True, True, True, True, False, 'position 8.7'], 8.8: [True, True, True, True, False, 'position 8.8'], 9.1: [True, True, True, True, False, 'position 9.1'], 9.2: [True, True, True, True, False, 'position 9.2'], 9.3: [True, True, True, True, False, 'position 9.3'], 9.4: [True, True, True, True, False, 'position 9.4'], 9.5: [True, True, True, True, False, 'position 9.5'], 9.6: [True, True, True, True, False, 'position 9.6'], 9.7: [True, True, True, True, False, 'position 9.7'], 9.8: [True, True, True, True, False, 'position 9.8']}

# startCorridorVis = 4.3
# finishCorridorVis = 1.3
# xAxisVis = 8
# yAxisVis = 9
# print(chr(9144)) # links
# print(chr(9145)) # rechts
# print(chr(9146)) # oben
# print(chr(9149)) # unten

# print(chr(9634)) # quada , alle True

#      Nord       East        South       West 
#      True       True        True        True 
countToVis = 0
lineRooms = ""

def countToVisChecker():
    global lineRooms
    global playgroundDicVis
    for ii in range(1, yAxisVis+1):
        for i in range(1,xAxisVis+1):
            i = i 
            s = str(ii)+"."+str(i)
            countToVis=0
            if playgroundDicVis[float(s)][0] == True:
                countToVis +=8 # Norden
            if playgroundDicVis[float(s)][1] == True:
                countToVis +=4 # East
            if playgroundDicVis[float(s)][2] == True:
                countToVis +=2 # South
            if playgroundDicVis[float(s)][3] == True:
                countToVis +=1 # West
            corridorVisualizer(countToVis)
        print(lineRooms)
        lineRooms =""

#################### visualizing from counter from Dic ###################
def corridorVisualizer(countToVis):
    ###### u can change all if's into a List #######     lineRooms += exampleList[countToVis] #########
    global lineRooms
    if countToVis == 0:
        lineRooms += chr(9580)
    if countToVis == 1:
        lineRooms += chr(9568)
    if countToVis == 2:
        lineRooms += chr(9577)
    if countToVis == 3:
        lineRooms += chr(9562)
    if countToVis == 4:
        lineRooms += chr(9571)
    if countToVis == 5:
        lineRooms += chr(9553)
    if countToVis == 6:
        lineRooms += chr(9565)
    if countToVis == 7:
        lineRooms += chr(9576)
    if countToVis == 8:
        lineRooms += chr(9574)
    if countToVis == 9:
        lineRooms += chr(9556)
    if countToVis == 10:
        lineRooms += chr(9552)
    if countToVis == 11:
        lineRooms += chr(9566)
    if countToVis == 12:
        lineRooms += chr(9559)
    if countToVis == 13:
        lineRooms += chr(9573)
    if countToVis == 14:
        lineRooms += chr(9569)
    if countToVis == 15:
        lineRooms += chr(9634)



############### ValueMoveChecker ################
counterToWin = 0
def valueMoveCheck():
    global playgroundDicVis
    global xAxisVis
    global yAxisVis
    global startCorridorVis
    global counterToWin
    realValueList = []
    tempList = []
    startCorridorVis = round((startCorridorVis - 1),2) # north
    if startCorridorVis < 1:
        startCorridorVis = round((startCorridorVis + 1),2)
    else:
        realValueList.append(0)
        if playgroundDicVis[startCorridorVis][4] == False:
            tempList.append(0)
        startCorridorVis = round((startCorridorVis + 1),2)

    startCorridorVis = round((startCorridorVis + 1),2) # south
    totalField = yAxisVis + (xAxisVis/10)
    totalField = round(totalField, 2)
    print(totalField)
    if startCorridorVis>totalField:
        startCorridorVis = round((startCorridorVis - 1),2)
        print("das ist süden wo es nicht geht")
    else:
        realValueList.append(2)
        print("das ist süden und es geht wunderbar")
        if playgroundDicVis[startCorridorVis][4] == False:
            tempList.append(2)
        startCorridorVis = round((startCorridorVis - 1),2)

    startCorridorVis = round((startCorridorVis - 0.1), 2) #west
    if (startCorridorVis % 1) == 0:
        startCorridorVis = round((startCorridorVis + 0.1), 2)
    else:
        realValueList.append(3)
        if playgroundDicVis[startCorridorVis][4] == False:
            tempList.append(3)
        startCorridorVis = round((startCorridorVis + 0.1), 2)

    startCorridorVis = round((startCorridorVis + 0.1), 2)
    if (startCorridorVis % 1 ) > round((xAxisVis/10),2) or startCorridorVis % 1 == 0: #east
        startCorridorVis = round((startCorridorVis - 0.1), 2)
    else:
        round(startCorridorVis,2)
        realValueList.append(1)
        if playgroundDicVis[startCorridorVis][4] == False:
            tempList.append(1)
        startCorridorVis = round((startCorridorVis - 0.1), 2)


    # print(realValueList)
    # print(tempList)
    if len(tempList) != 0:
        print(tempList,"Templist")
        valuebleMove = tempList[random.randint(0,len(tempList)-1)]
    else:
        print(realValueList,"Value List")
        valuebleMove = realValueList[random.randint(0,len(realValueList)-1)]

    
    counterToWin +=1
    return valuebleMove, counterToWin



while startCorridorVis != finishCorridorVis:
    playgroundDicVis[startCorridorVis][4] = True
    moveNESW, counterToWin = valueMoveCheck()

    #moveNESW = random.randint(0,3) # N North = 0, East = 1 , South = 2, West = 3
    if moveNESW == 0: # move North
        playgroundDicVis[startCorridorVis][0] = False
        startCorridorVis = round((startCorridorVis-1), 2)
        playgroundDicVis[startCorridorVis][2] = False
        # if startCorridorVis < 1:
        #     startCorridorVis +=1
        #     startCorridorVis = round(startCorridorVis, 2)
    if moveNESW == 1: # move East
        playgroundDicVis[startCorridorVis][1] = False
        startCorridorVis = round((startCorridorVis+0.1), 2)
        playgroundDicVis[startCorridorVis][3] = False
        
        # if (startCorridorVis %1) > (xAxisVis/10):
        #     startCorridorVis = round((startCorridorVis - 0.1),2)
            # startCorridorVis = round(startCorridorVis - 0.1 ,2)
    if moveNESW == 2: # move South
        playgroundDicVis[startCorridorVis][2] = False
        startCorridorVis = round((startCorridorVis + 1), 2)
        playgroundDicVis[startCorridorVis][0] = False
        # if startCorridorVis > yAxisVis:
        #     startCorridorVis -= 1
        #     startCorridorVis = round(startCorridorVis, 2)
    if moveNESW == 3: # move West
        playgroundDicVis[startCorridorVis][3] = False
        startCorridorVis = round((startCorridorVis-0.1), 2)
        playgroundDicVis[startCorridorVis][1] = False
        # if startCorridorVis % 1 == 0:
        #     print("West geht nicht !")
        #     startCorridorVis += 0.1
        #     startCorridorVis = round(startCorridorVis, 2)

    print(startCorridorVis)
    print("ich bin der Finish",finishCorridorVis)
    print("ich bin die XAchse",xAxisVis)
    print("ich bin die YAchse",yAxisVis)
    if startCorridorVis == finishCorridorVis:
        print("Es hat",counterToWin,"gebraucht")
        countToVisChecker()
    # if counter == 50:
        # break


def creatLoserWays():
    pass

