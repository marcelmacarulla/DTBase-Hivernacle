#Testing the login function--Fail, just for learning, i discovered bugs
import requests
import logging
from typing import Optional, Tuple

DEFAULT_USER_EMAIL= "a"
DEFAULT_USER_PASS = "b"

def login(
    email: str = DEFAULT_USER_EMAIL, password: Optional[str] = DEFAULT_USER_PASS
) -> Tuple[str, str]:
    """Log in to the backend server.

    If no user credentials are provided, use the default ones.

    Return an access token and a refresh token.
    """
    if password is None:
        raise ValueError("Must provide a password.")
    response = backend_call(
        "post",
        "/auth/login",
        {"email": DEFAULT_USER_EMAIL, "password": DEFAULT_USER_PASS},
    )
    if response.status_code != 200:
        raise BackendCallError(response)
    access_token = response.json()["access_token"]
    refresh_token = response.json()["refresh_token"]
    return access_token, refresh_token


username = 'marcel.macarulla@upc.edu'
password = 'Fjfk2kCthoF0eS7MfG6Eqb5'

login(username, password)

url = 'https://dtbasetest-backend.azurewebsites.net'
data = {'email': USER_NAME, 'password': PASSWORD}




response = requests.post(url, data=data)

print(response.text)