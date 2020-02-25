from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from createdFunctions import getFileMakerDatabase, getComputerName
from getpass import getpass

usernameMain = input('Username: ')
passwordMain = getpass('Password: ')
FM_Export = 'FM_ALL.csv'
computerList = getFileMakerDatabase(FM_Export)

if __name__ == '__main__':
    while True:
        cpuNumber = input('CPU NUMBER: ')
        computerName = getComputerName(computerList, cpuNumber)

        chrome_browser = webdriver.Chrome('./chromedriver.exe')
        chrome_browser.get('https://10.37.0.228/zenworks/jsp/index.jsp?pageid=deviceList')
        button = chrome_browser.find_element_by_id('details-button')
        button.click()
        button = chrome_browser.find_element_by_id('proceed-link')
        button.click()

        username = chrome_browser.find_element_by_id('username')
        username.clear()
        username.send_keys(usernameMain)

        password = chrome_browser.find_element_by_id('password')
        password.clear()
        password.send_keys(passwordMain)

        button = chrome_browser.find_element_by_id('loginButton')
        button.click()

        computerNameInput = chrome_browser.find_element_by_id('mainPage_deviceList_advancedSearch_defaultSearch')
        computerNameInput.clear()
        computerNameInput.send_keys(computerName)
        button = chrome_browser.find_element_by_id('mainPage_deviceList_advancedSearch_searchButton')
        button.click()

        button = chrome_browser.find_element_by_xpath('//*[@title="View Details"]')
        button.click()

        button = chrome_browser.find_element_by_xpath('//*[contains(text(), "Remote Control")]')
        button.click()

        select = Select(chrome_browser.find_element_by_id('mainPage_cmdHandlers_remoteControlWksDet_rmPopup_agentList'))
        select.select_by_index(1)

        time.sleep(1)

        button = chrome_browser.find_element_by_id('mainPage_cmdHandlers_remoteControlWksDet_rmPopup_okButton')
        button.click()

        time.sleep(1)



        actions = ActionChains(chrome_browser)
        actions.send_keys(Keys.ENTER)
        actions.perform()


        # alertPrompt = chrome_browser.switch_to_alert()
        # alertPrompt.accept()
        chrome_browser.quit()
