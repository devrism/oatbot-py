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

        reply = str(forecast['location']['name']) + " - currently " + str(forecast['current']['temp_f']) + "°F/"+ str(forecast['current']['temp_c']) + "°C and " + str(forecast['current']['condition']['text']) 
        for day in forecast['forecast']['forecastday']:
            reply += "\n\nForecast Date: " + str(day['date']) + ": " + str(day['day']['condition']['text'])
            reply += "\nAverage Temperature forecast: " + str(day['day']['avgtemp_f']) + "°F/" + str(day['day']['avgtemp_c']) + "°C"
    except: 
        reply = "I couldn't find your location! Maybe try using a zip code? 🙇"
        
    return reply
