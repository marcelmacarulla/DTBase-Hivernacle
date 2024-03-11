#Testing the SendData

import GreenHouseControl
#from GreenHouseControl.DTBase.SendData import SendData

USERNAME = "marcel.macarulla@upc.edu"
PASSWORD = "Fjfk2kCthoF0eS7MfG6Eqb5"

# Some made up example data.
data = {
    "measure_name": "Humidity",
    "unique_identifier": "Temperature and humidity sensor #1",
    "readings": [45.0, 50.0, 55.0],
    "timestamps": ["2024-01-02T00:00:00", "2024-01-02T00:01:00", "2024-01-02T00:02:00"]
}

send = GreenHouseControl.DTBase.SendSensorType()
t=send(data=data, dt_user_email=USERNAME, dt_user_password=PASSWORD)
print(t)