import sys
from WeatherInfo import WeatherInfo
from SoundChoiceEngine import SoundChoice

if (__name__ == '__main__'):
    modeIdx = sys.argv[1]
    latitude = sys.argv[2]
    longitude = sys.argv[3]

    mode_name = ['adrenaline', 'healing', 'deepsleep', 'focus', 'recovery']

    weatherInfo = WeatherInfo(latitude, longitude)
    weatherInfo.saveOpenWeatherDict()
    weatherMain = weatherInfo.getMainWeather()
    timeRange = weatherInfo.getClassifiedTimeName()

    engine = SoundChoice(int(modeIdx), weatherMain, timeRange)
    links = engine.getBestSound(algorithm='kangMapV1')

    for i, link in enumerate(links):
        if i == len(links) - 1:
            print(link, end='')
        else:
            print(link, end=',')

    sys.stdout.flush()
