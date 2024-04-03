#Testing the SendData
from datetime import datetime

import GreenHouseControl
#from GreenHouseControl.DTBase.SendData import SendData

import csv
send = GreenHouseControl.DTBase.SendData()

def convertir_fecha(fecha_original):
    # Convertir la cadena a un objeto datetime
    fecha_objeto = datetime.strptime(fecha_original, "%Y-%m-%d %H:%M:%S")

    # Crear una nueva fecha con la fecha requerida (enero 3 del año 2024)
    nueva_fecha = fecha_objeto.replace(month=fecha_objeto.month, day=fecha_objeto.day, hour=fecha_objeto.hour, minute=fecha_objeto.minute, second=0)

    # Formatear la nueva fecha en el formato deseado
    fecha_formateada = nueva_fecha.strftime("%Y-%m-%dT%H:%M:00")

    return fecha_formateada

# Ejemplo de uso de la función
fecha_original = "2024-02-23 18:50:00"
fecha_convertida = convertir_fecha(fecha_original)
print("Fecha convertida:", fecha_convertida)



#Variable="EPAR"
Variables=['ePAR', 'Temperature', 'RelativeHumidity', 'Co2', 'DewPoint', 'VPD', 'Pressure']
for Variable in Variables:
    # Abrir el archivo CSV
    with open('JoanB.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        columnas = reader.fieldnames
        print(columnas)
        temp=[]
        stamp=[]
        # Iterar sobre cada fila del CSV
        for row in reader:
            # Aquí puedes acceder a los valores de cada columna
            timestamp = row['date']
            #print(timestamp)
            timestamp = convertir_fecha(timestamp)
            #print(timestamp)
            try:
                temperatura = float(row[Variable])
                stamp.append(timestamp)
                #print(temperatura)
                temp.append(temperatura)
            except:
                #print("NA!")
                pass

    print(len(temp))
    print(len(stamp))
    # Construir el mensaje con los datos de la fila actual
    data = {
            "measure_name": Variable ,
            "unique_identifier": "GBF-S-GUARD-MB-01",
            "readings": temp,
            "timestamps": stamp,
            }
    #print(temp)
    #print(stamp)
    t = send.postData(data)

# Some made up example data.
data = {
    "measure_name": "Temperature",
    "unique_identifier": "GMOVE4EDU",
    "readings": [45.0, 50.0, 55.0],
    "timestamps": ["2024-01-02T00:00:00", "2024-01-02T00:01:00", "2024-01-02T00:02:00"]
}





