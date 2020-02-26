from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def getCredentials():
    userName = input('Username: ')
    passWord = getpass('Password: ')
    try:
        chrome_browser = webdriver.Chrome('./chromedriver.exe')
        chrome_browser.get('https://10.37.0.228/zenworks/jsp/index.jsp?pageid=deviceList')
        button = chrome_browser.find_element_by_id('details-button')
        button.click()
        button = chrome_browser.find_element_by_id('proceed-link')
        button.click()

        username = chrome_browser.find_element_by_id('username')
        username.clear()
        username.send_keys(userName)

        password = chrome_browser.find_element_by_id('password')
        password.clear()
        password.send_keys(passWord)

        button = chrome_browser.find_element_by_id('loginButton')
        button.click()

        computerNameInput = chrome_browser.find_element_by_id('mainPage_deviceList_advancedSearch_defaultSearch')
        credentials = {'username': userName, 'password': passWord}
        print('Login succeded.')
        chrome_browser.quit()
        return credentials
    except:
        chrome_browser.quit()
        print('\n\nInvalid logon credentials. Please try again.\n\n')
        getCredentials()

class Driver():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
    
    def getURL(self, browser):
        return self.driver.get(browser)
    
    def remoteControl(self, userName, passWord, computerName):
        self.getURL('https://10.37.0.228/zenworks/jsp/index.jsp?pageid=deviceList')
        button = self.driver.find_element_by_id('details-button')
        button.click()
        button = self.driver.find_element_by_id('proceed-link')
        button.click()
        username = self.driver.find_element_by_id('username')
        username.clear()
        username.send_keys(userName)
        password = self.driver.find_element_by_id('password')
        password.clear()
        password.send_keys(passWord)
        button = self.driver.find_element_by_id('loginButton')
        button.click()
        computerNameInput = self.driver.find_element_by_id('mainPage_deviceList_advancedSearch_defaultSearch')
        computerNameInput.clear()
        computerNameInput.send_keys(computerName)
        button = self.driver.find_element_by_id('mainPage_deviceList_advancedSearch_searchButton')
        button.click()
        button = self.driver.find_element_by_xpath('//*[@title="View Details"]')
        button.click()
        button = self.driver.find_element_by_xpath('//*[contains(text(), "Remote Control")]')
        button.click()
        select = Select(self.driver.find_element_by_id('mainPage_cmdHandlers_remoteControlWksDet_rmPopup_agentList'))
        select.select_by_index(1)
        time.sleep(1)
        button = self.driver.find_element_by_id('mainPage_cmdHandlers_remoteControlWksDet_rmPopup_okButton')
        button.click()
        time.sleep(1)
        self.driver.quit()

def remoteControl(computerName, userName, passWord):
    chrome_browser = webdriver.Chrome('./chromedriver.exe')
    chrome_browser.get('https://10.37.0.228/zenworks/jsp/index.jsp?pageid=deviceList')
    button = chrome_browser.find_element_by_id('details-button')
    button.click()
    button = chrome_browser.find_element_by_id('proceed-link')
    button.click()

    username = chrome_browser.find_element_by_id('username')
    username.clear()
    username.send_keys(userName)

    password = chrome_browser.find_element_by_id('password')
    password.clear()
    password.send_keys(passWord)

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

    #chrome_browser.quit()


if __name__ == '__main__':
    driver = Driver()
    driver.getURL('https://www.google.com')
    