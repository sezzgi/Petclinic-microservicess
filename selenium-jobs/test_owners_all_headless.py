from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

# Set chrome options for working with headless mode (no screen)
chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("window-size=1280,720")

# Update webdriver instance of chrome-driver with adding chrome options
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome("/Users/home/Desktop/chromedriver")

# Connect to the application
APP_IP = os.environ['MASTER_PUBLIC_IP']
url = "http://"+APP_IP.strip()+":30001/"

print(url)
driver.get(url)
sleep(3)

find_owners_link = driver.find_element(By.LINK_TEXT, "FIND OWNERS")
find_owners_link.click()
sleep(2)

# Verify that table loaded

verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

print("Table loaded")

driver.quit()