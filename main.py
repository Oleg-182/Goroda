from opencage.geocoder import OpenCageGeocode



def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2) # округляем до 2-ч знаков
            lon = round(results[0]['geometry']['lng'], 2) # округляем до 2-ч знаков
            return lat, lon
        else:
            return "Город не найден"
    except Exception as e:
        return f'Возникла ошибка: {e}'

key = 'a036f38429b74435af47ce1876f839d3'
city = 'Новосибирск'

coordinates = get_coordinates(city, key)

print(f'Координаты города {city}: {coordinates}')