import requests

API_KEY = "4ce59e3a36e72af6ceae27689330e56a"

def getCoordinatesByLocationName(city, country_code, limit):
    """
    Function that get the coordinates of a city by it's name and country code using
    openweather geocoding API
    :param city: the city (String)
    :param country_code: the country code (String)
    :param limit: the number of results (if there are multiple) (Integer)
    :return: a tuple that contains latitude and longitude of the location (in this order)
    """
    url = (f"https://api.openweathermap.org/geo/1.0/direct?"
           f"q={city},"
           f"{country_code}&"
           f"limit={limit}&"
           f"appid={API_KEY}")

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            info = posts[0]

            return (info["lat"], info["lon"])
        else:
            return False
    except Exception as exception:
        return False

def getWeatherByLatitudeLongitudeTime(latitude, longitude):
    """
    Function that gets the weather data for a city by it's latitude and longitude'
    :param latitude: the latitude
    :param longitude: the longitude
    :return: dictionary that contains the temperature, humidity, temperature_max and temperature_min
             (these are the keys)
    """
    url = (f"https://api.openweathermap.org/data/2.5/weather?"
           f"lat={latitude}&"
           f"lon={longitude}&"
           f"appid={API_KEY}")

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()

            return {
               "description": posts["weather"][0]["description"],
                "temperature": posts["main"]["temp"],
                "temperature_max": posts["main"]["temp_max"],
                "temperature_min": posts["main"]["temp_min"],
                "humidity": posts["main"]["humidity"],
            }
        else:
            return response.text
    except Exception as exception:
        return exception