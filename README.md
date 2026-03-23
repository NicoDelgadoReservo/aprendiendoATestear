
Basado en tutorial

https://www.selenium.dev/


# Requisitos
- [Requisitos](#requisitos)
  - [1. Tener python venv](#1-tener-python-venv)
  - [2. Instalar selenium](#2-instalar-selenium)
  - [3. Correr los test](#3-correr-los-test)
    - [New](#new)
    - [Producción](#producción)


## 1. Tener python venv

```
python -m venv venv
source venv/bin/activate
```
Si ya lo tienes instalado, solamente
```
source venv/bin/activate
```

## 2. Instalar selenium

```
pip install -r requirements.txt
```

## 3. Correr los test

### New
```
python /new/agenda-online/colombia.py
```

### Producción

Dejé configuradas varias agendas para testear los cambios de orden de los pasos para ser exhaustivos, solo cambia
esto, el resto de las configuraciones se mantienen iguales por ahora. Detalles en [notion](https://www.notion.so/softwarereservo/Testing-agenda-online-32675dda41668068bbb3d18b04028241)
```
python ./produccion/agenda-online/mexico.py
```

Para este test dejé también mejoras con args

--log para ver detalles en caso de que falle
--wait-time por si queremos modificar el tiempo, actualmente espera 0.5segundos (modificable) y 2 (fijo) cuando espera
confirmación.
--esconde-chrome parte en 1(no muestra crome), más que nada para no estorbar, pero si se quiere "ver el testing" se 
puede activar con --esconde-chrome=0

