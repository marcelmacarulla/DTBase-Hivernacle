import pandas as pd

from .DTBaseDataIngressv2 import DTBaseDataIngress

class ModBusSensors:
    """Representation of a collection of sensors."""
    def __init__(self):
        self.sensors=self.get_sensors()
        self.types=self.get_types()
        self.DTBaseDataIngress = DTBaseDataIngress()

        self.USERNAME = "marcel.macarulla@upc.edu"
        self.PASSWORD = "Fjfk2kCthoF0eS7MfG6Eqb5"


    def get_sensors(self):
        # Carga el archivo Excel en un DataFrame
        df = pd.read_excel('./ConfigFiles/DT-base-sensors.xlsx', sheet_name='DT-base-sensors', usecols='A:B',
                           skipfooter=1)

        # Elimina las filas que contienen valores NA
        df = df.dropna()

        data = df.to_dict(orient='records')
        #list= df['unique_identifier'].tolist()

        return data

    def get_types(self):
        # Leer el archivo Excel
        df = pd.read_excel('./ConfigFiles/DT-base-type-sensors.xlsx')

        # Agrupar por valores únicos en la primera columna
        grupos = df.groupby(['type_name'])

        # Lista para almacenar los resultados
        resultado = []

        # Iterar sobre los grupos
        for (type_name), grupo in grupos:
            # Diccionario para almacenar los resultados de este grupo
            grupo_resultado = {'type_name': type_name, 'measure_name': []}

            # Iterar sobre las filas del grupo y añadir las medidas a la lista
            for index, fila in grupo.iterrows():
                medida = {'name': fila['namev']}
                grupo_resultado['measure_name'].append(medida)

            # Agregar el diccionario al resultado
            resultado.append(grupo_resultado)

        return resultado

    def build_message(self):
        data=[]
        for sensor in self.sensors:
            type=sensor['type_name']
            # Buscar el diccionario con 'id' igual a 2
            for diccionario in self.types:
                if diccionario['type_name'] == type:
                    for type in diccionario['measure_name']:
                        data.append({
                            'measure_name': type['name'],
                            'unique_identifier': sensor['unique_identifier'],
                            'readings': [1.1],
                            'timestamps': ['2024-01-02T00:00:00'],
                        })
                    break
        return (data)

    def send_message(self):
        message = self.build_message()
        t=self.DTBaseDataIngress(data=message, dt_user_email=self.USERNAME, dt_user_password=self.PASSWORD)
        print(t)
        print(t[1])