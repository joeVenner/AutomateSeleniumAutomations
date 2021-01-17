from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os,wget


chromeDriver = "c:/users/joe/chromedriver.exe"

site =  'https://www.instagram.com/'

class browser:
    def __init__(self, driver,DEFAULT_TIMEOUT,delay):
        self.timeout = DEFAULT_TIMEOUT
        self.delay = delay
        self.driver = driver
        self.chrome_options = webdriver.ChromeOptions()

    def enable_download_headless(self,download_dir):
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        self.driver.execute("send_command", params)

    def element(self,xpath):
        self.Welement = WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def click(self):
            self.Welement.click()
            sleep(1)

    def send(self,text):
            self.Welement.send_keys(text)

    def get(self,site):
        self.driver.get(site)
        sleep(4)

    def Execute(self,scripts):
        self.driver.execute_script(scripts,self.Welement)

    def text(self):
        return self.Welement.text

    def attribute(self,att):
        return self.Welement.get_attribute(att)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=2')
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,executable_path=chromeDriver)
bot = browser(driver=driver,DEFAULT_TIMEOUT=20,delay=10)





bot.driver.maximize_window()



bot.get(site)

bot.element('//*[@id="loginForm"]/div/div[1]/div/label/input')
bot.send("yassir_lamo")
bot.element('//*[@id="loginForm"]/div/div[2]/div/label/input')
bot.send("testetest")
bot.element('//*[@id="loginForm"]/div/div[3]/button')
bot.click()

