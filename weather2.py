import requests

api_key = "08300f136892ed4d7b20785128bfb471"
city = "Nairobi"
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+ api_key+"&units=metric"

request = requests.get(url)
json = request.json()
# print(json)


description = json.get("weather")[0].get("description")
print("Today's forecast is", description)

temp_min = json.get("main").get("temp_min")
print("Today's min temperature is", temp_min)

temp_max = json.get("main").get("temp_max")
print("Today's max temperature is", temp_max)