import os

from Business.RequestsService import getCoordinatesByLocationName, getWeatherByLatitudeLongitudeTime
from Utils.Utility import kelvin_to_celsius


def clearScreen():
    """
    Function that clears the console using os library
    If this function doesn't work, you have to modify run configuration parameters by enabling
    the option "Emulate terminal in output console"
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def showMenu():
    """
    Function that shows the menu of the application and prints the related messages
    depending on the input entered by the user
    :return:
    """
    clearScreen()
    print("~~Weather app~~")
    print("If you want to exit the app, please enter \"exit\"")
    print("Otherwise, you can enter any message")
    if getInput() == "exit":
        return False

    clearScreen()
    print("~~Weather app~~")

    print("Please enter your city name: ")
    city = getInput()

    print("Please enter your country name: ")
    print("If you don't know it, you can find it on the link: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes")
    country_code = getInput()

    result = handleInput(city, country_code)

    print(f"Weather for {city}")
    print(f"Temperature is {kelvin_to_celsius(result['temperature'])}°C")
    print(f"Humidity is {result['humidity']}%")
    print(f"Max temperature is {kelvin_to_celsius(result['temperature_max'])}°C")
    print(f"Min temperature is {kelvin_to_celsius(result['temperature_min'])}°C")
    print("Enter any message to continue...")
    getInput()

def getInput():
    """
    Function that gets the input from the user
    :return: input (String)
    """
    return input()

def handleInput(city, country_code):
    """
    Function that handles the input from the user and make the operations
    related to the input
    :param city: the city (String)
    :param country_code: the country code (String)
    :return: dictionary that contains the temperature, humidity, temperature_max and temperature_min
             (these are the keys)
    """
    coordinates = getCoordinatesByLocationName(city, country_code, 1)

    try:
        latitude = coordinates[0]
        longitude = coordinates[1]
    except Exception:
        return False

    response = getWeatherByLatitudeLongitudeTime(latitude, longitude)

    return response