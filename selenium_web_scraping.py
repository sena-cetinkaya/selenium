from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://softmagicc.blogspot.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

print("Title: ", driver.title)
time.sleep(2)

print("Current Url: ", driver.current_url)
time.sleep(2)

blog1Click = driver.find_element(By.XPATH ,'//*[@id="Blog1"]/div[1]/div[1]/div/div/article/div/div/header/h2/a')
blog1Click.click()
time.sleep(3)

driver.back()
time.sleep(3)

driver.quit()