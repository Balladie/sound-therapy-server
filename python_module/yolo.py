def getClassifiedTimeName(dt, sunrise, sunset):
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

dt = 1583100000
sunrise = 1583129334
sunset = 1583172935

for i in range(0, 86400):
    if (getClassifiedTimeName(dt + i, sunrise, sunset) == 'ERROR'):
        print("dt:", dt)
        print("sunrise", sunrise)
        print("sunset", sunset)
        print("Error at:", i, dt+i)
