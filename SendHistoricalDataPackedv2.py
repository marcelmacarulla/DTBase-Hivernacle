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



Variables=['ePAR', 'Temperature', 'RelativeHumidity', 'Co2', 'DewPoint', 'VPD', 'Pressure']

for Variable in Variables:
    # Abrir el archivo CSV
    with open('07_02_24_Binafetv2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        columnas = reader.fieldnames
        print(columnas)
        temp=[]
        stamp=[]
        # Iterar sobre cada fila del CSV
        for row in reader:
            # Aquí puedes acceder a los valores de cada columna
            timestamp = row['date']
            ########
            # Diccionario para mapear los nombres de los meses a números de mes
            meses = {
                "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
            }

            # Divide la cadena de fecha en partes
            partes_fecha = timestamp.split()

            # Extrae los componentes de la fecha
            mes = partes_fecha[0]
            dia = int(partes_fecha[1])
            anio = int(partes_fecha[2])
            hora = datetime.strptime(partes_fecha[3], '%I:%M:%S')  # Analiza la hora
            ampm = partes_fecha[4]

            # Ajusta la hora si es PM
            if ampm == 'PM':
                hora = hora.replace(hour=hora.hour + 12)

            # Crea el objeto de fecha completa
            fecha_completa = datetime(anio, meses[mes], dia, hora.hour, hora.minute, hora.second)
            timestamp = fecha_completa.strftime("%Y-%m-%d %H:%M:%S")

            ####




            #print(timestamp)
            timestamp = convertir_fecha(timestamp)
            #print(timestamp)
            try:
                temperatura=row[Variable]
                temperatura = float(temperatura.replace(',','.'))
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
            "measure_name": Variable,
            "unique_identifier": "GM4-S-GUARD-MB-01",
            "readings": temp,
            "timestamps": stamp,
            }
    #print(temp)
    #print(stamp)
    t = send.postData(data)




