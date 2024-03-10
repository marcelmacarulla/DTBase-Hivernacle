# Testing the login, and obtaining the acces_token
from GreenHouseControl.DTBase.Utils import auth_backend_call, log_rest_response, login


username = "marcel.macarulla@upc.edu"
password = "Fjfk2kCthoF0eS7MfG6Eqb5"

access_token = login(username, password)[0]

print(access_token)

