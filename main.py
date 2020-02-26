from receiveInput import getFileMakerDatabase, getComputerName
from chromeAuto import remoteControl, getCredentials, Driver
import sys



if __name__ == '__main__':
    # program initialization
    try: 
        FM_Export = 'FM_ALL.csv'
        computerList = getFileMakerDatabase(FM_Export)
    except:
        print('Error loading database.')
        sys.exit()

    credentials = getCredentials()
    username = credentials['username']
    password = credentials['password']

    driver = Driver()

    while True:
        computerName = getComputerName(computerList)
        driver.remoteControl(username, password, computerName)
        #remoteControl(computerName, credentials['username'], credentials['password'])
