import json
import requests
from time import time, strftime, localtime
import sys


def getSunsign(sunsign, frequency):

    # import horoscope API
    request_url = "http://horoscope-api.herokuapp.com/horoscope/" + frequency + "/" + sunsign.title()

    response = requests.get(request_url)

    response_text = json.loads(response.text)

    horoscope_today = response_text["horoscope"]
    print("Horoscope Insights: " + horoscope_today)

    symbol = response_text["sunsign"]
    print("Sunsign: " + symbol)

    if frequency == "today":
        print("Today: " + response_text["date"] + "\nHave a good one!")
    else:
        print(frequency.title() + ": " + response_text[frequency] + "\nHave a good one!")

zodiacsigns = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "stagittarius", "capricorn", "aquarius", "pisces"]
frequencies = ["today", "week", "month", "year"]

    # capture user input
while True:
    sunsign = input("Welcome to Zodiac in Everyday Life app! Astrology helps you get " + '''
        xx                      xx     xx
          xx         xx  xx       xx  xx
            xx     x   xx   x       xx
             xx   x          x      xx
            xx      x       x       xx
       xxxxx          x  x          xx''' + "\nPlease input your sunsign:")
    if not sunsign in zodiacsigns:
        print("OOPS, WRONG MESSAGE! Please select your sunsign from 12 zodiac signs: aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, stagittarius, capricorn, aquarius, pisces.")
        continue
    break

while True:
    frequency = input("Please select a time frames from today, week, month, year:")
    if not frequency in frequencies:
        print("OOPS, WRONG MESSAGE! Please select a time frame from today, week, month, year:")
        continue
    break

getSunsign(sunsign, frequency)
