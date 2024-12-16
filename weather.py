import requests
url = "https://api.openweathermap.org/data/2.5/weather?lat=35.6895&lon=139.6917&appid=422e66f36efa164a3af0781e671c5d81"

response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  print(f"{data['name']} City")
  print(f"Weather: {data['weather'][0]['description']}")
  print(f"Humidity: {data['main']['humidity']}")
  print(f"Sunrise coord: {data['sys']['sunrise']}")
  print(f"Sunset coord: {data['sys']['sunset']}")

else:
  print(f"Error en la solicitud: {response.status_code}")
  print(response.json()["results"])