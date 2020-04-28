# URL Fornat https://assets-runtime-production-oxed-oup.avallain.net/274109_bks_MaaHL_1104_gdc15_xxcg50.pdf
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/Users/aldrin0n9/Documents/Python Projects/Profile")
driver = webdriver.Opera(executable_path="/Users/aldrin0n9/Documents/Python Projects/operadriver", options=options)

url = "https://assets-runtime-production-oxed-oup.avallain.net/274109_bks_MaaHL_1104_gdc15_xxcg50.pdf"
for x in range (1,6):
    for y in range (1,21):
        for z in range (100, 120):
            url = "https://assets-runtime-production-oxed-oup.avallain.net/274"+str(z)+"_bks_MaaHL_110"+str(x)+"_gdc"+str(y)+"_xxcg50.pdf"
            driver.get(url)
            print(url)