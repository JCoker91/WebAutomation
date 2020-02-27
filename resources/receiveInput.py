import csv
import sys
from os import system

def displayMenu():
    print("""
1) Remote Control
2) CPU Info
3) Google Password Reset
4) Clever Verification
    """)

# checks input from command line and returns a dictionary of settings
def getCommandLineArgs():
    argDict = {'show_window': False, 'window_mode': 'OFF'}
    for arg in sys.argv[1:]:
        try:
            if arg == '-w':
                argDict['show_window'] = True 
                argDict['window_mode'] = 'ON'
            else:
                argDict['show_window'] = False
                argDict['window_mode'] = 'OFF'
        except IndexError:
            argDict['show_window'] = False
            argDict['window_mode'] = 'OFF'
    return argDict

def getMenuSelection():
    displayMenu()
    selection = input('Selection: ')
    return selection

def getFileMakerDatabase(csvFile):
    with open(csvFile, newline='') as csvfile:
        myDict = {}
        fieldnames = ['Computer_Name', 'CPU']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        try:
            for row in reader:
                myDict[f"{row['CPU']}"] = row['Computer_Name']
        except:
            print(f"Fail at {row['Computer_Name']}, {row['CPU']}")
        return myDict

def getCPUNumber(databaseDict):
    while True:
        cpuNumber = input('CPU Number: ')
        if cpuNumber != '':
            if cpuNumber in databaseDict:
                return cpuNumber
            else:
                system('clear')
                print(f'\nCPU number {cpuNumber} not found in database.\n')
    
def getComputerNameFromCPUNumber(cpuNumber, databaseDict):
    return databaseDict[cpuNumber]

if __name__ == "__main__":
    database = getFileMakerDatabase('resources/FM.csv')
    cpuNumber = getCPUNumber(database)
    computerName = getComputerNameFromCPUNumber(cpuNumber, database)
    print(cpuNumber)
    print(computerName)
    