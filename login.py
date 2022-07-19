# My first test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/home/hiho/chromedriver_linux64/chromedriver')

#open the webpage
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
driver.find_element(By.ID, 'id_username').send_keys("usuariopeluqueria")
driver.find_element(By.ID, 'id_password').send_keys("123")

formulario = driver.find_element(By.TAG_NAME, 'form')
inputs_del_formulario = formulario.find_elements(By.TAG_NAME, 'input')

for input in inputs_del_formulario:
    if input.get_attribute("value") == "Ingresar":
        ingresar_boton = input

input.click()

### Login ###
### Crear cita ###
# TODO:
# - Agregar "camino" para clientedemo (agenda por box)
# - Mejorar creacion de citas para que busque primero en mismo día y luego cambie
# de semana o día

calendario = driver.find_element(By.CLASS_NAME, 'fc-agenda-slots')
slot6 = calendario.find_element(By.CLASS_NAME, 'fc-slot6')
next_button = driver.find_element(By.ID, 'next')
calendario_con_eventos = driver.find_element(By.ID, 'calendar')

def trata_de_levantar_modal_de_reserva(elemento_para_reservar, next_button):
    hizo_reserva = False
    while not hizo_reserva:
        try:
            elemento_para_reservar.click()
            hizo_reserva = True
        except:
            next_button.click()
            sleep(1)

trata_de_levantar_modal_de_reserva(slot6, next_button)
cantidad_eventos_antes_agregar = len(calendario_con_eventos.find_elements(By.CLASS_NAME, 'fc-event')) - 1
print("Eventos antes de pushear nuevo evento", cantidad_eventos_antes_agregar)

barra_oficial = driver.find_element(By.ID, 'barra_oficial')
profesional_actual = barra_oficial.find_element(By.TAG_NAME, 'button').get_attribute("title")

agenda_select = driver.find_element(By.ID, 'id_servicio')
agenda_select = Select(agenda_select)
agenda_select.select_by_visible_text(profesional_actual)

reservar_button = driver.find_element(By.ID, 'Reservar')
reservar_button.click()
sleep(1)

cantidad_eventos_despues_agregar = len(calendario_con_eventos.find_elements(By.CLASS_NAME, 'fc-event'))
print("Eventos después de pushear nuevo evento", cantidad_eventos_despues_agregar)

### Crear cita ###
