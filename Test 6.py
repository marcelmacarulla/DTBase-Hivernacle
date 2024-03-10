#Testing the minimalingress.py modified to only add data

from GreenHouseControl.DTBase.DTBaseDataIngress import DTBaseDataIngress

username = "marcel.macarulla@upc.edu"
password = "Fjfk2kCthoF0eS7MfG6Eqb5"


# Some made up example data.
data = {
    "measure_name": "Humidity",
    "unique_identifier": "Temperature and humidity sensor #1",
    "readings": [45.0, 50.0, 55.0],
    "timestamps": ["2024-01-02T00:00:00", "2024-01-02T00:01:00", "2024-01-02T00:02:00"]
}
ingresser = DTBaseDataIngress()

# Calling the ingresser will call the get_service_data method you wrote above, and then
# send all the requests you specified to the backend (create the sensor type, create the
# sensor, insert data). It also handles user authentication with the given email and
# password. Any arguments you want to pass to get_service_data should be passed to the
# ingresser instead, _as keyword arguments_. Positional arguments will not work.
#
# If you run the same ingresser multiple times (e.g. once a minute with new data), it
# will try to create the same sensor type and sensors again and again. That's okay, the
# backend will just ignore the requests to create duplicates. Likewise if you try to
# insert duplicate data entries, they will simply get ignored.

ingresser(data=data, dt_user_email=username, dt_user_password=password)