#Testing the SendData

import pandas as pd
from GreenHouseControl.DTBase.SendSensorTypev2 import SendSensorType

USERNAME = "marcel.macarulla@upc.edu"
PASSWORD = "Fjfk2kCthoF0eS7MfG6Eqb5"


# Leer el archivo Excel
df = pd.read_excel('./ConfigFiles/DT-base-type-sensors.xlsx')

# Agrupar por valores únicos en la primera columna
grupos = df.groupby(['type_name', 'description'])

# Lista para almacenar los resultados
resultado = []

# Iterar sobre los grupos
for (type_name,  description), grupo in grupos:
    # Diccionario para almacenar los resultados de este grupo
    grupo_resultado = {'type_name': type_name, 'description': description, 'measures': []}

    # Iterar sobre las filas del grupo y añadir las medidas a la lista
    for index, fila in grupo.iterrows():
        medida = {'name': fila['namev'], 'units': fila['units'], 'datatype': fila['datatype']}
        grupo_resultado['measures'].append(medida)

    # Agregar el diccionario al resultado
    resultado.append(grupo_resultado)

send = SendSensorType()
t=send(data=resultado, dt_user_email=USERNAME, dt_user_password=PASSWORD)
print(t[0].text)
print(t)