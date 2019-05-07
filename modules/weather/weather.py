import os
from apixu.client import ApixuClient

def getWeather(input, weatherKey):
    #TODO documentation
    #if ' help ' in input:
        #return helpDocs("WEATHER", input) 

    input = input.content
    input = input[9:]

    try:
        weatherClient = ApixuClient(weatherKey)

        search = weatherClient.search(q=input)

        forecast = weatherClient.forecast(q=input, days=2)
        current = weatherClient.current(q=input)

        reply = "**" + str(current['location']['name']) + "** " + convertWeatherToEmoji(current['current']['condition']['text']) + " currently " + str(current['current']['temp_f']) + "°F/"+ str(current['current']['temp_c']) + "°C and " + str(current['current']['condition']['text']).lower() 
        reply += "\nCurrent wind speed: " + str(current['current']['wind_mph']) + " mph/" + str(current['current']['wind_kph']) + " kph"
        for day in forecast['forecast']['forecastday']:
            reply += "\n\n" + convertWeatherToEmoji(str(day['day']['condition']['text'])) + " " + str(day['date']) + ": " + str(day['day']['condition']['text']).lower()
            reply += "\nAvg. Temperature: " + str(day['day']['avgtemp_f']) + "°F/" + str(day['day']['avgtemp_c']) + "°C"

    except Exception as e: 
        reply = "I couldn't find your location! Maybe try using a zip code? 🙇"
        print(e)
        
    return reply

def convertWeatherToEmoji(condition):
    condition = condition.lower()
    emoji = ''
    if 'torrential rain shower' in condition:
        emoji = '🌊'
    elif 'thunder' in condition:
        emoji = '🌩'
    elif 'rain' in condition:
        emoji = '🌧'
    elif 'fog' in condition:
        emoji = '🌫'
    elif 'partly cloudy' in condition:
        emoji = '⛅'
    elif 'cloudy' in condition:
        emoji = '☁'
    elif 'sunny' in condition or 'clear' in condition:
        emoji = '☀'
    return emoji