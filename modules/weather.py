#!/usr/bin/env python
# -*- coding: utf-8 -*-
import willie
import forecastio

API_KEY = "41cbdafc2dc5571e85712340b993a278"
lat = "48.3058255"
lng = "14.2838517"

responses = {
    "clear-day": "It's fucking alright.",
    "clear-night": "It's fucking dark.",
    "rain": "It's fucking raining.",
    "snow": "It's fucking snowing.",
    "sleet": "Fucking snow with rain.",
    "wind": "It's fucking windy.",
    "fog": "Fucking fifty shades of grey.",
    "cloudy": "Fucking clouds everywhere.",
    "partly-cloudy-day": "Some fucking clouds.",
    "partly-cloudy-night": "Fucking dark with clouds.",
}

@willie.module.commands('weather')
def weather(bot, trigger):
    forecast = forecastio.load_forecast(API_KEY, lat, lng)
    today = forecast.hourly()
    bot.reply(today.summary)

@willie.module.commands('fuckingweather')
def weather(bot, trigger):
    forecast = forecastio.load_forecast(API_KEY, lat, lng)
    now = forecast.currently()
    if now.icon in responses:
        bot.reply(responses[now.icon])
    else:
        bot.reply("I have no fucking clue!")

@willie.module.commands('temp')
def temp(bot, trigger):
    forecast = forecastio.load_forecast(API_KEY, lat, lng)
    now = forecast.currently()
    dump = "%.2f°C, feels like %.2f°C" %(now.temperature, now.apparentTemperature)
    bot.reply(dump)

