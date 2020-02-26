import csv

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

def getComputerName(databaseDict):
    test = False
    while test == False:
        cpuNumber = input('CPU Number: ')
        if cpuNumber != '':
            try:
                computerName = databaseDict[cpuNumber]
                print(f"Connecting to {computerName}")
                test = True
                return computerName
            except KeyError as err:
                print(f"CPU number {err} not found in database.")