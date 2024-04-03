#Testing the SendData

import pandas as pd
from GreenHouseControl.DTBase.DeleteSensorType import DeleteSensorType

USERNAME = "marcel.macarulla@upc.edu"
PASSWORD = "Fjfk2kCthoF0eS7MfG6Eqb5"


# Leer el archivo Excel
df = pd.read_excel('./ConfigFiles/DT-base-type-sensors-weather-station.xlsx')

# Agrupar por valores únicos en la primera columna
grupos = df.groupby(['type_name', 'description'])

# Lista para almacenar los resultados
resultado = []

# Iterar sobre los grupos
for (type_name,  description), grupo in grupos:
    # Diccionario para almacenar los resultados de este grupo
    grupo_resultado = {'type_name': type_name}

    # Agregar el diccionario al resultado
    resultado.append(grupo_resultado)

send = DeleteSensorType()
t=send(data=resultado, dt_user_email=USERNAME, dt_user_password=PASSWORD)
print(t[0].text)
print(t[0])