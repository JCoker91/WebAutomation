from receiveInput import getFileMakerDatabase, getComputerName
from chromeAuto import remoteControl, getCredentials
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

    while True:
        computerName = getComputerName(computerList)
        remoteControl(computerName, credentials['username'], credentials['password'])
