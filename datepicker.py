# import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\My Downloads\chromedriver_win32\chromedriver")
driver:WebDriver=webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)  # switch to frame
year="2020"
month="June"
date="30"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("09/30/2022")
#mm/dd/yyyy

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break
    else:
        # driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
        driver.find_element(By.XPATH,"//span[normalize-space()='Prev']").click()
#select date
dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")     # selected all dates
for d in dates:
    if d.text==date:
      d.click()
      break
# time.sleep(3)
# driver.close()
