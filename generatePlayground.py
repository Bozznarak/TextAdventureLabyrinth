import random

def createPlayground():

    # Playground
    yAxis = random.randint(5,9) # hoehe
    xAxis = random.randint(5,9) # breite
    playgroundDic = {}
    for ii in range(1, yAxis+1): # to south
        for i in range(1,xAxis+1): # to east
            i = i 
            s = str(ii)+"."+str(i)
            playgroundDic[float(s)] = [True, True , True, True, False, "position "+str(s)]

    # Finish Position
    # darf nur am Rand sein, also y = 1 oder y= letzte Einheit und x = 1 oder x = letzte Einheit
    LROrUD = random.randint(0,1)
    if LROrUD == 0: #Left or Right
        leftOrRight = random.randint(0,1)
        if leftOrRight == 0: # Left
            finishCorridor = random.randint(1,yAxis)
            finishCorridor = finishCorridor + 0.1
            finishCorridor = round(finishCorridor,2)
        if leftOrRight == 1: # Right
            finishCorridor = random.randint(1,yAxis)
            finishCorridor = round((finishCorridor + (xAxis/10)),2)
    if LROrUD == 1: # Up or Down
        UpOrDown = random.randint(0,1)
        if UpOrDown == 0: # Up
            finishCorridor = random.randint(1, xAxis)
            finishCorridor = round(((finishCorridor/10)+1),2)
        if UpOrDown == 1: # down
            finishCorridor = random.randint(1, xAxis)
            finishCorridor = round(((finishCorridor/10)+yAxis),2)

    # Start Poisition
    x1 = random.randint(1,xAxis)
    y1 = random.randint(1,yAxis)
    s1 = str(y1)+"."+str(x1)
    startCorridor = float(s1)
    # startCorridor = round(random.uniform(1.1, float(s1)), 1)
    # while True:
    #     if startCorridor == int(startCorridor):
    #         x1 = random.randint(0,xAxis)
    #         y1 = random.randint(0,yAxis)
    #         s1 = str(x1)+"."+str(y1)
    #         startCorridor = round(random.uniform(1.1, float(s1)), 1)
    #     else:
    #         break
    print(playgroundDic)
    return playgroundDic, startCorridor, finishCorridor,xAxis,yAxis






