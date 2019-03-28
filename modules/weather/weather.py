import pyowm

def getWeather(input, weatherKey):
    #TODO
    #if ' help ' in input:
        #return helpDocs("WEATHER", input) 

    input = input.content
    input = input[9:]

    #documentation 
    
    owm = pyowm.OWM(weatherKey)

    observation = owm.weather_at_place(input)
    reply = observation.get_weather()

    return reply
