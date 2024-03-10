#This python script is to test the login
from GreenHouseControl.DTBase.Utils import backend_call, login, auth_backend_call

username = "marcel.macarulla@upc.edu"
password = "Fjfk2kCthoF0eS7MfG6Eqb5"

print(login(username, password))