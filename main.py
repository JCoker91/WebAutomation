from resources import receiveInput
from resources.chromeAutomation import Driver
from os import system
from sys import exit
import sys

FM_Export = 'resources/FM.csv'

if __name__ == '__main__':
    system('clear')

    # get command line arguments to set parameters
    configuration = receiveInput.getCommandLineArgs()

    # initialize dictionary from exported FileMaker csv
    try: 
        FileMakerDatabase = receiveInput.getFileMakerDatabase(FM_Export)
    except Exception as err:
        print(f'\n\nError initializing database. Error: {err}\n\n')
        exit()

    # initialize web driver
    try:
        driver = Driver(configuration)
        print(f"Starting program\nBrowser Window Mode: {configuration['window_mode']}\n")
    except Exception as err:
        print(f"\n\nError initializing web driver. Error: {err}\n\n")
        exit()

    # validate and initialize ZENWorks credentials
    credentials = driver.getZENWorksCredentials()
    username = credentials['username']
    password = credentials['password']

    # Run program to remote into computer
    while True:
        cpuNumber = receiveInput.getCPUNumber(FileMakerDatabase)
        computerName = receiveInput.getComputerNameFromCPUNumber(cpuNumber, FileMakerDatabase)
        driver.remoteControlZENWorks(username, password, computerName)
