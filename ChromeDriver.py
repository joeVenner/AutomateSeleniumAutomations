from selenium import webdriver
import wget,platform
import getpass,requests
from zipfile import ZipFile

###########################################################
# ChromeDriver will be Downloaded to your User Home repo  #
# Contact me : ylafrimi@gmail.com                         #
# Github : JoeVenner                                      #
###########################################################



driver = webdriver.Chrome()

if 'browserVersion' in driver.capabilities:
    chromeVersion = driver.capabilities['browserVersion'][0:2]
else:
    chromeVersion = driver.capabilities['version'][0:2]
driver.close()

osname = platform.system()
if osname == 'Darwin':
    os = "mac64"
    ChromeDriverpath = f"/Volumes/Mac/Users/{getpass.getuser()}/"
elif osname == 'Windows':
    os = "win32"
    ChromeDriverpath = f"c:/users/{getpass.getuser()}/"
elif osname == 'Linux':
    os = "linux64"
    ChromeDriverpath = f"/home/{getpass.getuser()}/"
else:
    print(f"Unknown OS '{osname}', Please manuelly Download the ChromeDriver!")

chromedriverVersion = requests.get(f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chromeVersion}")

wget.download(f"https://chromedriver.storage.googleapis.com/{chromedriverVersion.text}/chromedriver_{os}.zip",ChromeDriverpath)

with ZipFile(f'chromedriver_{os}.zip', 'r') as zipf:
   zipf.extractall()
