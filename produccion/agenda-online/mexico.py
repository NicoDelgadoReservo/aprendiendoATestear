import argparse
import logging
import sys
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar logging
def setup_logging(enable_logging=False):
  if enable_logging:
    logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(levelname)s - %(message)s',
      handlers=[
        logging.FileHandler('test_agendas.log'),
        logging.StreamHandler(sys.stdout)
      ]
    )
  else:
    # Deshabilitar logs si no se solicita
    logging.basicConfig(level=logging.CRITICAL)

def log_info(message, always_print=False):
  if always_print:
    print(message)
  else:
    logging.info(message)

def log_error(message):
  logging.critical(message)

# Relleno de Pasos
def rellenar_paso_horario(driver, wait_time):
  log_info("rellenar_paso_horario")
  boton_continuar = WebDriverWait(driver, wait_time).until(
      EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continuar') or contains(text(),'Agendar')]"))
  )
  boton_continuar.click() 
  time.sleep(1)

def rellenar_paso_datos(driver, wait_time):
  log_info("rellenar_paso_datos")
  input_rut = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.ID, "rut"))
  )

  input_rut.send_keys("HEGJ820506M10")
  boton_agendar = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Agendar') or contains(text(), 'Continuar')]"))
  )
  boton_agendar.click()

def rellenar_paso_profesionales(driver, wait_time):
  log_info("rellenar_paso_profesionales")
  dropdown = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Selecciona Profesional')]"))
  )
  dropdown.click()
  primera_opcion = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='stf-select-option']"))
  )
  primera_opcion.click()
  boton_continuar = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continuar') or contains(text(),'Agendar')]"))
  )
  boton_continuar.click()

def rellenar_paso_tratamiento(driver, wait_time):
  log_info("rellenar_paso_profesionales")
  dropdown = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Selecciona Tratamiento')]"))
  )
  dropdown.click()
  primera_opcion = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='stf-select-option']"))
  )
  primera_opcion.click()
  boton_continuar = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continuar') or contains(text(),'Agendar')]"))
  )
  boton_continuar.click()

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
  },
  "profesionales": {
    "test": (By.XPATH, "//div[contains(text(),'Selecciona Profesional')]"),
    "accion": rellenar_paso_profesionales
  },
  "tratamiento": {
    "test": (By.XPATH, "//div[contains(text(),'Selecciona Tratamiento')]"),
    "accion": rellenar_paso_tratamiento
  }
}

def identificar_paso_actual(driver):
  """Identifica qué paso está visible actualmente"""
  wait_corto = WebDriverWait(driver, 2)
  
  for nombre_paso, paso in pasos.items():
    log_info(f"será paso '{nombre_paso}'?")
    try:
      wait_corto.until(
        EC.visibility_of_element_located(paso["test"])
      )
      return nombre_paso, pasos[nombre_paso]["accion"]
    except:
      continue
  return None, None

def testear_agendas(wait_time=0.5, esconde_chrome=1):

  try:
    #specify the path to chromedriver.exe (download and save on your computer)
    options = webdriver.ChromeOptions()
    if esconde_chrome=="1":
      options.add_argument("--headless=new") 
    driver = webdriver.Chrome(options=options)
    with open('./produccion/agenda-online/agendas.json', 'r') as file:
      agendas = json.load(file)
    for agenda in agendas:
      log_info(f"Testeando Agenda {agenda['titulo']}")
      driver.get(agenda["url"])
      sin_confirmar = True
      paso = 1
      while (sin_confirmar):
        nombre_paso, accion = identificar_paso_actual(driver)
        if not nombre_paso:
          log_error(f"f, No pudimos encontrar en qué tipo de paso estamos (paso {paso}) para agenda {agenda['titulo']}")
        if nombre_paso == "confirmacion":
          log_info(f"Agenda {agenda['titulo']} OK")
          sin_confirmar = False
        else:
          accion(driver, wait_time)
        paso += 1
    log_info("Todo ok", True)
  except Exception as e:
    log_error(f"f, Error: {e}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Test de agendas con Selenium')
  parser.add_argument('--log', action='store_true', help='Habilitar logging detallado')
  parser.add_argument('--wait-time', type=float, default=0.5, help='Tiempo de espera para WebDriverWait (default:1)')
  parser.add_argument('--esconde-chrome', default="1", help='No muestra el navegador, 0 si se quiere ver')
  args = parser.parse_args()
  
  setup_logging(args.log)
  log_info(f"Configuración: wait_time={args.wait_time}s, log={args.log}, esconde_chrome={args.esconde_chrome}", always_print=True)
  
  testear_agendas(wait_time=args.wait_time, esconde_chrome=args.esconde_chrome)