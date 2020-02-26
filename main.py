from resources.receiveInput import getFileMakerDatabase, getComputerNameFromCPU
from resources.chromeAuto import Driver
from os import system
from sys import exit


if __name__ == '__main__':

   # initialize dictionary from exported FileMaker csv
    system('clear')
    FM_Export = 'FM_ALL.csv' 
    try: 
        FileMakerDatabase = getFileMakerDatabase(FM_Export)
    except Exception as err:
        print(f'\n\nError initializing database. Error: {err}\n\n')
        exit()

    # initialize web driver
    try:
        driver = Driver()
    except Exception as err:
        print(f"\n\nError initializing web driver. Error: {err}\n\n")
        exit()

    # validate and initialize ZENWorks credentials
    credentials = driver.getZENWorksCredentials()
    username = credentials['username']
    password = credentials['password']

    # Run program
    while True:
        computerName = getComputerNameFromCPU(FileMakerDatabase)
        driver.remoteControlZENWorks(username, password, computerName)
