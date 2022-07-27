import requests

api_key = "" #Gererate the API Key in https://openweathermap.org/
city = input("What is the city?\n")
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric"+"&appid="+api_key

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forecast in", city, "is", description)
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min, "grau Celcius")
temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_min, "grau Celcius")
