import requests

city = input("What is the city?\n")

def get_weather_desc_and_temp():
    api_key = "860afc85c18322e3684a0a44b69a0b81"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric"+"&appid="+api_key

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}

def main():
    # Print the results
    weather_dict = get_weather_desc_and_temp()    
    print("Today's forecast in", city, "is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'), "graus Celcius")
    print("The maximum temperature is", weather_dict.get('temp_max'), "graus Celcius")

main()
