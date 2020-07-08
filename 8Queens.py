import random,sys
n=8
pop=10
maxFitness=28
hardstop=5
pblMut=.03

def randomPositions(): #generate random positions 
    return [ random.randint(0, n-1) for _ in range(n) ]

def findHorClash(lstBStr):   
    lsthorClashStr = [lstBStr.count(col)-1 for col in lstBStr]
    horClashCnt = int(sum(lsthorClashStr)/2)   
    return horClashCnt

def findDiagClash(lstBStr):
    diaClashStr=[]

    for colInd in range(n):
        rowEnt=lstBStr[colInd]
        rowUpInd=rowEnt
        rowDnInd=rowEnt
        colNextInd=colInd
        colPrevInd=colInd
        cnt=0
        crossChk = lambda col,rowUp,rowDn,rowEnt: 1 if col>=0 and (rowEnt==rowUp or rowEnt==rowDn) else 0
        for i in range(n-(colInd+1)):
            rowUpInd+=1
            rowDnInd-=1
            colNextInd+=1
            colPrevInd-=1
            rowNextEnt=lstBStr[colNextInd]
            rowPrevEnt=lstBStr[colPrevInd]
            lstBStr[colNextInd]
            cnt+=crossChk(colNextInd,rowUpInd,rowDnInd,rowNextEnt)
            cnt+=crossChk(colPrevInd,rowUpInd,rowDnInd,rowPrevEnt)
            #print(str(colInd) + "=" + str(rowEnt) + "->" + str(rowUpInd) + "-<" + str(rowDnInd) + "=" + str(rowNextEnt) + "=" + str(rowPrevEnt))
        diaClashStr.append(cnt)
    diaClashCnt = int(sum(diaClashStr)/2)   
    return diaClashCnt  


def geneticIteration(popBStr):
    return popBstr[random.randint(0, n-1)]

if __name__ == "__main__":
    fitness=1
    loopincr=0
    popBstr =[randomPositions() for _ in range(pop)]

    while maxFitness!=fitness and loopincr<hardstop:
        loopincr+=1
        popProb=[]
        for i in popBstr:
            listPosStr = geneticIteration(popBstr)
            horClashCnt = findHorClash(listPosStr)
            diaClashCnt = findDiagClash(listPosStr)
            fitness = int(maxFitness - (horClashCnt + diaClashCnt))
            probability = fitness/maxFitness
            print( "****(" + str(horClashCnt) + "," + str(diaClashCnt) + ")***" + str(fitness))
            popProb.append(probability)
    
    print(popBstr)
    print(popProb)
    popZipProb = zip(popBstr,popProb)
    #print(popZipProb)
  
        
   


