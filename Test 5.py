#Testing the minimalingress.py

from GreenHouseControl.DTBase.MinimalIngress import MinimalExampleDataIngress

username = "marcel.macarulla@upc.edu"
password = "Fjfk2kCthoF0eS7MfG6Eqb5"


# Some made up example data.
data = {
    "temperatures": [20.0, 21.0, 22.0],
    "humidities": [50.0, 51.0, 52.0],
    "timestamps": ["2021-01-01T00:00:00", "2021-01-01T00:01:00", "2021-01-01T00:02:00"]
}
ingresser = MinimalExampleDataIngress()

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