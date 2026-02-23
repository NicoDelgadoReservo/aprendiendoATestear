from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

#En WIP 23/02/26
try:
  #specify the path to chromedriver.exe (download and save on your computer)
  driver = webdriver.Chrome()

  driver.get("http://localhost:8005/inicioreservo/bienvenida/6ac7e100-10ed-11f1-8216-d6b9ec5c274b/")

  boton = driver.find_element(By.XPATH, "//span[text()='Comenzar']")
  boton.click()
except Exception as e:
  print(f"configurar_nuevo_cliente.py, x Error: {e}")