# My first test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
  #specify the path to chromedriver.exe (download and save on your computer)
  driver = webdriver.Chrome()

  #open the webpage
  driver.get("https://new.reservo.cl/makereserva/agenda/O0CVRxh0f0tY0K114O60X6H6B5I5Xh")
  '''
  Pasos de la agenda:
  1. Tratamiento
  2. Profesional
  3. Día y Hora
  4. Ingresar Datos
  '''

  ### Paso 1 ###
  dropdown = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.CLASS_NAME, "stf-select__inner-wrapper"))
  )
  dropdown.click()
  time.sleep(0.1)

  primera_opcion = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='249806']"))
  )
  primera_opcion.click()
  time.sleep(0.1)

  boton_continuar = WebDriverWait(driver, 1).until(
      EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continuar')]"))
  )
  boton_continuar.click()
  time.sleep(1)

  ### Paso 2 ###

  dropdown = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Selecciona Profesional')]"))
  )
  dropdown.click()
  time.sleep(0.1)

  primera_opcion = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='44710']"))
  )
  primera_opcion.click()
  time.sleep(0.1)

  boton_continuar.click()
  time.sleep(1)

  ### Paso 3 ###
  #Confiamos en que hay siguiente hora

  boton_continuar.click()
  time.sleep(1)

  ### Paso 4 ###
  input_rut = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.ID, "rut"))
  )

  input_rut.send_keys("1-9")
  boton_agendar = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Agendar')]"))
  )
  boton_agendar.click()
  
  mensaje_ok = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Información de su cita')]"))
  )
  if mensaje_ok:
    print("TODO OK :)")

except Exception as e:
  print(f"f, x Error: {e}")