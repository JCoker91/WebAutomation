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

def getComputerName(computer_List, cpu_Number):
    computerName = computer_List[cpu_Number]
    print(f"Connecting to {computerName}")
    return computerName