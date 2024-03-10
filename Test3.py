#This python file is to test the connectivity with the server
import requests

username = "marcel.macarulla@upc.edu"
password = "Fjfk2kCthoF0eS7MfG6Eqb5"


url = 'https://dtbasetest-backend.azurewebsites.net/auth/login'
data = {"email": username, "password": password}

print (data)

request_type = "post"
request_func = getattr(requests, request_type)


#response = request_func(url, {"email": str(username), "password": str(password)})



response = requests.post(url, json=data)

#access_token = response.json()["access_token"]
#refresh_token = response.json()["refresh_token"]

print(response.text)

#print(access_token)
#print(refresh_token)

sensor = {
  "measure_name": 1,
  "unique_identifier": 1,
  "readings": [
    0,
  ],
  "timestamps": [
    "2024-03-10T21:02:32.077Z"
  ]
}
print ("......")
sensor = requests.post(url, json=sensor)

print(sensor.text)