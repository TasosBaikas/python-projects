from random import randrange,seed,shuffle
from datetime import datetime
from math import floor,ceil

seed(None)

Arrays = 100

def inputChecker(rowOrColumn):
    while(1):
            try:
                NumberOfRowsOrColumns = int(input(f"give {rowOrColumn} for the matrix (must be more than 2):"))
                print(" ")
                if NumberOfRowsOrColumns > 2:
                    break
                else:
                    print(f"wrong {rowOrColumn[:-1]} input!!")  
                    print(" ")
            except:
                SystemExit(0)
    return NumberOfRowsOrColumns


def userInput():
    for i in range(10):
        print(" ")
    print("----------- The SOS statistic -----------")
    for i in range(3):
        print(" ")
    rows = inputChecker("rows")
    columns = inputChecker("columns")
    wantToSeeTheArrays = int(input(f"Do you want to see the {Arrays} Arrays; (1 for Yes or 0 for No) :"))
    print(" ")
    if wantToSeeTheArrays == 1:
        wantToSeeTheArrays = 1
    else:    
        wantToSeeTheArrays = 0

    return rows,columns,wantToSeeTheArrays

def makeSosArray(rows,columns):
    sosTempList = []
    if (randrange(0,2)): #for not to place more S or O if the matrix has an odd number of cells
        for cell in range(floor(rows*columns/2)):
            sosTempList.append("S")
        for cell in range(ceil(rows*columns/2)):
            sosTempList.append("O")
    else:
        for cell in range(ceil(rows*columns/2)):
            sosTempList.append("S")
        for cell in range(floor(rows*columns/2)):
            sosTempList.append("O")
    shuffle(sosTempList)

    def fillSosArray():
        matrix = []
        for row in range(rows):
            matrix.append([])
            for column in range(columns):  
                matrix[row].append(sosTempList[row*(columns) + column])
        
        return matrix


    filledMatrix = fillSosArray()
    return filledMatrix

def checkForSos(rows,columns,sosArray):
    def checkRows():
        sosFound = 0
        for row in range(rows):
            for column in range(columns - 2):
                if sosArray[row][column] == "S" and sosArray[row][column + 1] == "O" and sosArray[row][column + 2] == "S" :
                    sosFound += 1
        return sosFound
    
    def checkColumns():
        sosFound = 0
        for column in range(columns):
            for row in range(rows - 2):
                if sosArray[row][column] == "S" and sosArray[row + 1][column] == "O" and sosArray[row  + 2][column] == "S" :
                    sosFound += 1
        return sosFound
        
    def checkDiagonals():
        sosFound = 0
        for row in range(rows - 2):
            #first time across the array
            for column in range(columns - 2):
                if sosArray[row][column] == "S" and sosArray[row + 1][column + 1] == "O" and sosArray[row + 2][column + 2] == "S" :
                    sosFound += 1
            #second time across the array
            for column in range(columns - 2):
                if sosArray[row][-column - 1] == "S" and sosArray[row + 1][-column - 2] == "O" and sosArray[row + 2][-column - 3] == "S" :
                    sosFound += 1
        return sosFound

                 
    #first we are looking at the rows
    sosFoundInRows = checkRows()
    sosTriesInRows = rows*(columns - 2)
    #Next we are looking at the columns
    sosFoundInColumns = checkColumns()
    sosTriesInColumns = columns*(rows - 2)
    #Next we are looking for the diagonals
    sosFoundInDiagonals = checkDiagonals()
    sosTriesInDiagonals = (rows - 2)*2

    totalSosFound = sosFoundInRows + sosFoundInColumns + sosFoundInDiagonals
    totalSosTries = sosTriesInRows + sosTriesInColumns + sosTriesInDiagonals

    return totalSosFound,totalSosTries

def printArrays(rows,sosArray,sosFound,sosTries):
    print("----------------")
    for row in range(rows):
        print(sosArray[row])

    print("SOS found = " + str(sosFound))
    print("Checks that were made = " + str(sosTries))


def main():
    rows,columns,wantToSeeTheArrays = userInput()

    totalSosFound = 0
    totalSosTries = 0 

    for game in range(Arrays):
        sosArray = makeSosArray(rows,columns)
        sosFound,sosTries = checkForSos(rows,columns,sosArray)
        if wantToSeeTheArrays:
            printArrays(rows,sosArray,sosFound,sosTries)

        totalSosFound += sosFound
        totalSosTries += sosTries
        

    average = totalSosFound/totalSosTries
    print("====================================")
    print(f"Total SOS found in the {Arrays} Arrays = {totalSosFound}")
    print(f"Total checks for SOS that were made in the {Arrays} Arrays = {totalSosTries}" + "\n")
    print(f"The average SOS that were found in the {Arrays} Arrays is {average*100}%")
    

main()