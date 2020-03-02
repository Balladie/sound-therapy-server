import json
import WeatherInfo

lat = 0
lon = 0

weatherInfo = WeatherInfo.WeatherInfo(lat, lon)
weatherInfo.saveOpenWeatherDict(customInput=True)
weatherInfo.printWeather()
print()
print(weatherInfo.getMainWeather())
print(weatherInfo.getClassifiedTimeName())
