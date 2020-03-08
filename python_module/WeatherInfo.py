import requests
import json

class WeatherInfo:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.appid = "4eea9f438846d244011468b6c4284214"
        self.weather = {}

    def saveOpenWeatherDict(self, customInput=False):
        if customInput:
            with open('./data/for_test.json') as json_file:
                self.weather = json.load(json_file)
        else:
            url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(self.lat) + "&lon=" + str(self.lon) + "&appid=" + self.appid
            self.weather = requests.get(url).json()

    def printWeather(self, raw=False):
        if raw:
            print(json.dumps(self.weather))
        else:
            print(json.dumps(self.weather, indent=4, sort_keys=True))

    def getMainWeather(self):
        weatherId = self.weather['weather'][0]['id']
        if weatherId >= 700 and weatherId < 800:
            return 'Atmosphere'
        return self.weather['weather'][0]['main']

    # 6 kinds of time ranges
    def getClassifiedTimeName(self):
        dt = self.weather['dt']
        sunrise = self.weather['sys']['sunrise']
        sunset = self.weather['sys']['sunset']
        
        tMorning = sunrise + 3600
        tEvening = sunset - 3600

        trDaySlots = (tEvening - tMorning) / 3
        tNoon = tMorning + trDaySlots
        tAfternoon = tNoon + trDaySlots

        tNight = tEvening + 10800
        tDawn = tMorning - 12600

        if tMorning <= dt and dt < tNoon:
            return 'Morning'
        elif tNoon <= dt and dt < tAfternoon:
            return 'Noon'
        elif tAfternoon <= dt and dt < tEvening:
            return 'Afternoon'
        elif tEvening <= dt and dt < tNight:
            return 'Evening'
        elif tDawn <= dt and dt < tMorning:
            return 'Morning'
        else:
            return 'Night'

    def getHumidity(self):
        return self.weather['main']['humidity']

if (__name__ == '__main__'):
    weatherInfo = WeatherInfo(37, 126)
    weatherInfo.saveOpenWeatherDict()
    weatherInfo.printWeather()
    print(weatherInfo.getMainWeather())
    print(weatherInfo.getClassifiedTimeName())
