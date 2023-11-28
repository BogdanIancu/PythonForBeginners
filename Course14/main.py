import webbrowser
import requests

# webbrowser.open("https://google.com")

location = input("Please enter location: ")
params = {"appid": "7b10426ee90376dc3d6525f847128b35", "q": location, "mode": "json", "units": "metric", "lang": "en"}
response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
print(response.text)
print(response.status_code)

json_response = response.json()
print()
print("Temperature: ", json_response["main"]["temp"])
print("Description: ", json_response["weather"][0]["description"])

