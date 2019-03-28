import pyowm

def getWeather(input, weatherKey):
    #TODO documentation
    #if ' help ' in input:
        #return helpDocs("WEATHER", input) 

    input = input.content
    input = input[9:]
    
    owm = pyowm.OWM(weatherKey)
    reply = ""

    try:
        observationList = owm.weather_at_places(input, searchtype='like')

        #for obs in observationList:
            #reply = reply + obs.get_location().get_name() + ", " +  obs.get_location().get_country() + "\n"
            #print([func for func in dir(obs.get_location()) if callable(getattr(obs.get_location(), func))])
        if observationList:
            reply = "My weather module is under construction! But here's my best try: \n\n" + str(observationList[0].get_weather())
        else:
            reply = "I couldn't find your location, but I'm working hard to improve! 🙇"

    except Exception as e:
        print(e)
        reply = "Error, please try again later 🙇 maybe try using your zip code instead?"
        
    return reply
