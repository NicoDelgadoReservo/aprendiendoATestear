# My first test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def rellenar_paso_horario(driver):
  print("rellenar_paso_horario")
  boton_continuar = WebDriverWait(driver, 1).until(
      EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continuar') or contains(text(),'Agendar')]"))
  )
  boton_continuar.click() 
  time.sleep(1)

def rellenar_paso_datos(driver):
  print("rellenar_paso_datos")
  input_rut = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.ID, "rut"))
  )

  input_rut.send_keys("HEGJ820506M10")
  boton_agendar = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Agendar') or contains(text(), 'Continuar')]"))
  )
  boton_agendar.click()

pasos = {
  "confirmacion": {
    "test": (By.XPATH, "//div[contains(text(),'Información de su cita')]"),
    "accion": None
  },
  "horario": {
    "test": (By.XPATH, "//div[starts-with(@id,'Seleccionadiayhora')]"),
    "accion": rellenar_paso_horario
  },
  "datos": {
    "test": (By.ID, "rut"),
    "accion": rellenar_paso_datos
  }
}

def identificar_paso_actual(driver):
  print("identificar_paso_actual")
  """Identifica qué paso está visible actualmente"""
  wait_corto = WebDriverWait(driver, 2)
  
  for nombre_paso, paso in pasos.items():
    print("será ", nombre_paso)
    try:
      wait_corto.until(
        EC.visibility_of_element_located(paso["test"])
      )
      print("síp")
      return nombre_paso, pasos[nombre_paso]["accion"]
    except:
      continue
  print("F")
  return None, None

def testear_agendas():

  try:
    #specify the path to chromedriver.exe (download and save on your computer)
    driver = webdriver.Chrome()

    #open the webpage
    agendas = [
      #1Datos 2Horario
      "https://agendamiento.reservo.cl/makereserva/agenda/U0pyzis0e0vAO61d8T55eHW0x946UO",
      #1Horario 2Datos
      "https://agendamiento.reservo.cl/makereserva/agenda/t0axK9n0c0K7RD4k8j25R7h0E4V6gQ",
    ]
    for agenda in agendas:
      print("Agenda ", agenda)
      driver.get(agenda)
      sin_confirmar = True 
      while (sin_confirmar):
        nombre_paso, accion = identificar_paso_actual(driver)
        if not nombre_paso:
          print(f"f, No pudimos encontrar en qué paso estamos")
        if nombre_paso == "confirmacion":
          print(f"Agenda {agenda} OK")
          sin_confirmar = False
        else:
          accion(driver)
      time.sleep(2)

    


  except Exception as e:
    print(f"f, x Error: {e}")

testear_agendas()