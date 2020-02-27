from time import sleep
from sys import exit
from os import system
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from selenium.webdriver.common.keys import Keys

class Driver():
    # receives a dictionary of key values for settings
    # - -w show_window [True, False]
    # - -w window_mode ['ON', 'OFF']
    # - -i show_details [True, False] TODO 
    # - -i detailed_view ['ON', 'OFF'] TODO 
    # - -n create_comments [True, False] TODO
    # - -n comment_mode ['ON', 'OFF'] TODO
    # - -l create_log [True, False] TODO
    # - -l logging_mode ['ON', 'OFF'] TODO
    def __init__(self, configurationDict):
        self.configuration = configurationDict
    
    # gets the URL and sets the configurations for windowed vs headless
    def getURL(self, browser):
        if self.configuration['show_window'] == True:
            self.driver = webdriver.Chrome('./chromedriver.exe')
            self.driver.get(browser)
        else:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome('./chromedriver.exe',options=options)
            self.driver.get(browser)
    
    # gets ZENWorks credentials from user and validates before exitting function
    def getZENWorksCredentials(self):
        print('\nZENWorks login credentials')
        userName = input('Username: ')
        passWord = getpass('Password: ')
        print('\nVerifying ZENWorks credentials. Please wait...\n')
        self.getURL('https://10.37.0.228/zenworks/jsp/index.jsp?pageid=deviceList')
        try:
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
        except:
            system('clear')
            print('\n\nUnable to reach logon page. Please check the URL and try again.\n\n')
            self.driver.quit()
            exit()
        try:
            self.driver.find_element_by_id('mainPage_deviceList_advancedSearch_defaultSearch')
            self.driver.quit()
            credentials = {'username': userName, 'password': passWord}
            system('clear')
            print('\n\nLogin succeded.\n\n')
            return credentials
        except:
            self.driver.quit()
            system('clear')
            print('\n\nInvalid logon credentials. Please try again.\n\n')
            self.getZENWorksCredentials()

    # main function for remoting into a computer
    def remoteControlZENWorks(self, userName, passWord, computerName):
        print(f'\nConnecting to {computerName}...\n')
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
        sleep(1)
        button = self.driver.find_element_by_id('mainPage_cmdHandlers_remoteControlWksDet_rmPopup_okButton')
        button.click()
        sleep(1)
        #self.driver.quit()
