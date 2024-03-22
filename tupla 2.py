import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('./ConfigFiles/DT-base-type-sensors.xlsx')

# Agrupar por valores únicos en la primera columna
grupos = df.groupby(['type_name', 'description'])

# Lista para almacenar los resultados
resultado = []

# Iterar sobre los grupos
for (type_name,  description), grupo in grupos:
    # Diccionario para almacenar los resultados de este grupo
    grupo_resultado = {'type_name': type_name, 'description': description, 'medidas': []}

    # Iterar sobre las filas del grupo y añadir las medidas a la lista
    for index, fila in grupo.iterrows():
        medida = {'name': fila['namev'], 'units': fila['units'], 'datatype': fila['datatype']}
        grupo_resultado['medidas'].append(medida)

    # Agregar el diccionario al resultado
    resultado.append(grupo_resultado)

# Imprimir el resultado
for r in resultado:
    print(r)

print(resultado[0]['medidas'])