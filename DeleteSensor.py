#Testing the SendData

import pandas as pd
from GreenHouseControl.DTBase.DeleteSensor import DeleteSensor

USERNAME = "marcel.macarulla@upc.edu"
PASSWORD = "Fjfk2kCthoF0eS7MfG6Eqb5"


# Leer el archivo Excel
df = pd.read_excel('./ConfigFiles/DT-base-sensors-weather-station.xlsx')

# Agrupar por valores únicos en la primera columna
grupos = df.groupby(['unique_identifier'])

# Lista para almacenar los resultados
resultado = []

# Iterar sobre los grupos
for (unique_identifier), grupo in grupos:
    # Diccionario para almacenar los resultados de este grupo
    grupo_resultado = {'unique_identifier': unique_identifier}

    # Agregar el diccionario al resultado
    resultado.append(grupo_resultado)

send = DeleteSensor()
t=send(data=resultado, dt_user_email=USERNAME, dt_user_password=PASSWORD)
print(t[0].text)
print(t[0])