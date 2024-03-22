#The purpose of this script is to send the sensors registred in the DT-base-sensors.xlsx, located in
#in the folder ConfigFiles.

from GreenHouseControl.DTBase.SendSensorsv2 import SendSensorsv2

import pandas as pd
import json
from datetime import datetime

from openpyxl import load_workbook
import os

#user name and password to access to DTBase
USERNAME = "marcel.macarulla@upc.edu"
PASSWORD = "Fjfk2kCthoF0eS7MfG6Eqb5"

# Carga el archivo Excel en un DataFrame
df = pd.read_excel('./ConfigFiles/DT-base-sensors.xlsx', sheet_name='DT-base-sensors', usecols='A:D', skipfooter=1)

# Elimina las filas que contienen valores NA
df = df.dropna()

# Convierte el DataFrame en una lista de diccionarios
data = df.to_dict(orient='records')

# Send all sensors to the DTBase
send = SendSensorsv2()
objects=send(data=data, dt_user_email=USERNAME, dt_user_password=PASSWORD)

# Lista para almacenar los detalles
detalles = []

# Iterar sobre cada objeto en la lista para mandar los detalles de la respuesta
for objet in objects:
    # Obtener el texto del objeto
    text = objet.text

    # Convertir el texto a JSON
    try:
        json_data = json.loads(text)

        # Obtener el campo 'detail' si está presente
        if 'detail' in json_data:
            detalles.append(json_data['detail'])
        else:
            detalles.append(None)  # Si no hay detalle, agregar None

    except json.JSONDecodeError:
        detalles.append(None)  # Si no se puede decodificar como JSON, agregar None

# Obtener la ruta al archivo Excel donde guardar los detalles
nombre_archivo = 'DT-base-sensors.xlsx'
ruta_carpeta = 'ConfigFiles'  # Nombre de la carpeta donde se encuentra el archivo Excel

# Combinar la ruta de la carpeta con el nombre del archivo
ruta_excel = os.path.join(ruta_carpeta, nombre_archivo)

# Cargar el archivo Excel existente
workbook = load_workbook(ruta_excel)

# Seleccionar la hoja en la que deseas trabajar
hoja = workbook.active

# Agregar los elementos de lista_F a la columna F
for i, elemento in enumerate(detalles, start=2):
    hoja[f'F{i}'] = elemento
    hoja[f'E{i}'] = datetime.now()

# Guardar los cambios en el archivo Excel
workbook.save(ruta_excel)

print("Sensors updated in DTBase")



