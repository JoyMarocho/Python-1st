# import requests

# def get_weather_desc_and_temp():
#     api_key = "08300f136892ed4d7b20785128bfb471"
#     city = "Nairobi"
#     url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+ api_key+"&units=metric"

#     request = requests.get(url)
#     json = request.json()
#     # print(json)

#     description = json.get("weather")[0].get("description")
#     temp_min = json.get("main").get("temp_min")
#     temp_max = json.get("main").get("temp_max")
    
#     return {'description': description,
#             'temp_min': temp_min,
#             'temp_max': temp_max 
#             }

# # Print the resuluts
# weather_dict = get_weather_desc_and_temp()
# print("Today's forecast is", weather_dict.get('description'))
# print("Today's min temperature is", weather_dict.get('temp_min'))
# print("Today's max temperature is", weather_dict.get('temp_max'))



################### ORGANIZING our main code ###############
#################

import requests

def get_weather_desc_and_temp():
    api_key = "08300f136892ed4d7b20785128bfb471"
    city = "Nairobi"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+ api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()
    # print(json)

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    
    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max 
            }

def main():
    weather_dict = get_weather_desc_and_temp()
# Print the resuluts
    print("Today's forecast is", weather_dict.get('description'))
    print("Today's min temperature is", weather_dict.get('temp_min'))
    print("Today's max temperature is", weather_dict.get('temp_max'))

main ()

