# My first test
from selenium import webdriver

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/home/hiho/chromedriver_linux64/chromedriver')

#open the webpage
driver.get("http://localhost:8005/")

