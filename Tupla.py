from typing import Tuple, List, Dict #I had to add Tuple

data = {
    "measure_name": "Humidity",
    "unique_identifier": "Temperature and humidity sensor #1",
    "readings": [45.0, 50.0, 55.0],
    "timestamps": ["2024-01-02T00:00:00", "2024-01-02T00:01:00", "2024-01-02T00:02:00"]
}


def get_service_data(data: Dict[str, list]) -> List[Tuple[str, dict]]:
    # Create a sensor type.
    return_value: List[Tuple[str, dict]] = [
        (
            "/sensor/insert-sensor-readings",
            {
                "measure_name": data["measure_name"],
                "unique_identifier": data["unique_identifier"],
                "readings": data["readings"],
                "timestamps": data["timestamps"],
            },
        ),
    ]
    print(return_value)
    return return_value


get_service_data(data)

import pandas as pd

# Carga el archivo Excel en un DataFrame
df = pd.read_excel('./ConfigFiles/DT-base-sensors.xlsx', sheet_name='DT-base-sensors', usecols='A:D', skipfooter=1)

# Elimina las filas que contienen valores NA
df = df.dropna()

# Convierte el DataFrame en una lista de diccionarios
lista_de_diccionarios = df.to_dict(orient='records')

# Muestra la lista de diccionarios
print(lista_de_diccionarios)

# Muestra las primeras filas del DataFrame
print(df.head())





