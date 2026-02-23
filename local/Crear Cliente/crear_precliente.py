from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

try:
  #specify the path to chromedriver.exe (download and save on your computer)
  driver = webdriver.Chrome()

  driver.get("http://localhost:8005/")

  ### Login ###
  nav_bar_elements = driver.find_element(By.ID, 'navBarLanding')
  buttons_in_nav_bar = nav_bar_elements.find_elements(By.TAG_NAME, 'button')

  for button in buttons_in_nav_bar:
    if button.text == "Inicia sesión":
      iniciar_boton = button

  if iniciar_boton:
    iniciar_boton.click()

  # Rellenamos formulario
  driver.find_element(By.NAME, 'username').send_keys("usuariopeluqueria")
  driver.find_element(By.ID, 'password').send_keys("123")
  driver.find_element(By.XPATH, "//span[contains(text(),'Iniciar sesión')]").click()
  sleep(2)
  driver.get('http://localhost:8005/inicioreservo/crearprecliente/')
  driver.find_element(By.ID, 'id_nombre_cliente').send_keys("Test Agenda online Box")
  driver.find_element(By.ID, 'id_correos_contacto').send_keys("ndelgado+testAO1@reservo.cl")
  Select(driver.find_element(By.ID, 'id_pais')).select_by_index(1)  
  Select(driver.find_element(By.ID, 'id_rubro')).select_by_index(1)
  driver.find_element(By.ID, 'id_capacidad_atencion').send_keys(0)
  driver.find_element(By.ID, 'id_precio_acordado').send_keys(0)
  Select(driver.find_element(By.ID, 'id_currency')).select_by_index(0)
  driver.find_element(By.ID, 'id_tipo_agenda_1').click()
  driver.find_element(By.ID, 'id_numero_agendas').send_keys(0)
  driver.find_element(By.ID, 'id_numero_usuarios').send_keys(0)
  driver.find_element(By.ID, 'id_numero_profesionales').send_keys(0)

  guardar = driver.find_element(By.XPATH, "//input[@type='button' and @value='Guardar']")
  guardar.click()
  
  sleep(10)
  
  driver.quit()  
except Exception as e:
  print(f"crear_precliente.py, x Error: {e}")