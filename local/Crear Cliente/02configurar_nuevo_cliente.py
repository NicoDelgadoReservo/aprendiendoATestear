from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
def paso0():
  button_comenzar = driver.find_element(By.XPATH, "//span[contains(text(),'Comenzar')]")
  button_comenzar.click()
  
def paso1():
  print("Paso 1...")
  input_id_nombre = driver.find_element(By.ID, 'id_nombre')
  input_id_nombre.clear()
  input_id_nombre.send_keys("Test Agenda online Box")
  
  input_id_direccion = driver.find_element(By.ID, 'id_direccion')
  input_id_direccion.clear()
  input_id_direccion.send_keys("Calle falsa 123")
  
  input_id_telefono = driver.find_element(By.ID, 'id_telefono')
  input_id_telefono.clear()
  input_id_telefono.send_keys("99999999")
  
  input_id_correo_corporativo = driver.find_element(By.ID, 'id_correo_corporativo')
  input_id_correo_corporativo.clear()
  input_id_correo_corporativo.send_keys("ndelgado+testAO1@reservo.cl")
  
  input_id_sitio_web = driver.find_element(By.ID, 'id_sitio_web')
  input_id_sitio_web.clear()
  input_id_sitio_web.send_keys("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

  button_guardar = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Guardar']")
  button_guardar.click()
  print("Paso 1 OK")

def paso2():
  print("Paso 2...")
  input_id_rut = driver.find_element(By.XPATH, "//input[@id='id_rut']")
  input_id_rut.clear()
  input_id_rut.send_keys("11111111-1")

  input_id_correo_finanzas = driver.find_element(By.XPATH, "//input[@id='id_correo_finanzas']")
  input_id_correo_finanzas.clear()
  input_id_correo_finanzas.send_keys("ndelgado+testAO1@reservo.cl")

  input_id_telefono_finanzas = driver.find_element(By.XPATH, "//input[@id='id_telefono_finanzas']")
  input_id_telefono_finanzas.clear()
  input_id_telefono_finanzas.send_keys("99999999")

  input_id_razon_social = driver.find_element(By.XPATH, "//input[@id='id_razon_social']")
  input_id_razon_social.clear()
  input_id_razon_social.send_keys("razón social")

  input_id_giro = driver.find_element(By.XPATH, "//input[@id='id_giro']")
  input_id_giro.clear()
  input_id_giro.send_keys("giro")

  input_id_region = driver.find_element(By.XPATH, "//input[@id='id_region']")
  input_id_region.clear()
  input_id_region.send_keys("region")

  input_id_comuna = driver.find_element(By.XPATH, "//input[@id='id_comuna']")
  input_id_comuna.clear()
  input_id_comuna.send_keys("comuna")

  input_id_ciudad = driver.find_element(By.XPATH, "//input[@id='id_ciudad']")
  input_id_ciudad.clear()
  input_id_ciudad.send_keys("ciudad")

  input_id_direccion = driver.find_element(By.XPATH, "//input[@id='id_direccion']")
  input_id_direccion.clear()
  input_id_direccion.send_keys("Calle falsa 123")

  
  button_guardar = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Guardar']")
  button_guardar.click()
  print("Paso 2 OK")

def paso3():
  print("Paso 3...")
  inputs_check_acepto = driver.find_elements(By.XPATH, "//input[@id='check_acepto']")
  print("inputs_check_acepto", inputs_check_acepto)
  if inputs_check_acepto:
    inputs_check_acepto[0].click()
    button_confirmar = driver.find_element(By.XPATH, "//button[@type='button' and @onclick='enviar_form()']")
    button_confirmar.click()
  else:
    button_confirmar = driver.find_element(By.PARTIAL_LINK_TEXT, "Siguiente")
    button_confirmar.click()
  sleep(10)
  print("Paso 3 OK")
  
def paso4():
  print("Paso 4...")
  sleep(2)
  print("Paso 4 OK")

#En WIP 23/02/26
try:
  #specify the path to chromedriver.exe (download and save on your computer)
  driver = webdriver.Chrome()

  driver.get("http://localhost:8005/inicioreservo/bienvenida/6ac7e100-10ed-11f1-8216-d6b9ec5c274b/")
  titulo_saltarse_primer_paso = driver.find_elements(By.XPATH, "//h1[contains(text(),'Creación de cuenta Test Agenda online Box')]")
  titulo_iniciamos_paso_1 = driver.find_elements(By.XPATH, "//h2[contains(text(),'Datos centro')]")
  titulo_iniciamos_paso_2 = driver.find_elements(By.XPATH, "//h2[contains(text(),'Datos facturación')]")
  titulo_iniciamos_paso_3 = driver.find_elements(By.XPATH, "//h4[contains(text(),'Términos y condiciones')]")
  titulo_iniciamos_paso_4 = driver.find_elements(By.XPATH, "//h2[contains(text(),'Creación de usuario')]")
  
  print("titulo_iniciamos_paso_1: ", titulo_iniciamos_paso_1)
  print("titulo_iniciamos_paso_2: ", titulo_iniciamos_paso_2)
  print("titulo_iniciamos_paso_3: ", titulo_iniciamos_paso_3)
  print("titulo_iniciamos_paso_4: ", titulo_iniciamos_paso_4)
  if len(titulo_saltarse_primer_paso) < 1:
    paso0()
    paso1()
    paso2()
    paso3()
    paso4()
  elif len(titulo_iniciamos_paso_1) == 1:
    paso1()
    paso2()
    paso3()
    paso4()
  elif len(titulo_iniciamos_paso_2) == 1:
    paso2()
    paso3()
    paso4()
  elif len(titulo_iniciamos_paso_3) == 1:
    paso3()
    paso4()
  elif len(titulo_iniciamos_paso_4) == 1:
    paso4()
  else:
    print("Nos saltamos todo")
  sleep(5)
  driver.quit()
  
except Exception as e:
  print(f"configurar_nuevo_cliente.py, x Error: {e}")