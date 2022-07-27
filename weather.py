import requests

api_key = "860afc85c18322e3684a0a44b69a0b81"
city = input("What is the city?\n")
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric"+"&appid="+api_key

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forecast in", city, "is", description)
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min, "graus Celcius")
temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_min, "graus Celcius")
