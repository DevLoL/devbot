#!/usr/bin/env python
# -*- coding: utf-8 -*-
import willie
import forecastio
import mosquitto

API_KEY = "41cbdafc2dc5571e85712340b993a278"
lat = "48.3058255"
lng = "14.2838517"

dungeon = {"temp": 0, "hum": 0}
mainroom = {"temp": 0, "hum": 0}

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

def on_message(client, data, msg):
    try:
        if(msg.topic == "devlol/h19/dungeon/DHT21/temp"):
            dungeon["temp"] = float(msg.payload.replace('\t', ''))
        if(msg.topic == "devlol/h19/dungeon/DHT21/hum"):
            dungeon["hum"] = float(msg.payload.replace('\t', ''))
        if(msg.topic == "devlol/h19/mainroom/DHT21/temp"):
            mainroom["temp"] = float(msg.payload)
        if(msg.topic == "devlol/h19/mainroom/DHT21/hum"):
            mainroom["hum"] = float(msg.payload)
    except:
        print "Invalid Messages injected!"
        pass

client = mosquitto.Mosquitto()
client.connect("test.mosquitto.org")
client.on_message = on_message
client.subscribe("devlol/#")

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
    dump = "Mainroom: %.2f°C, Dungeon: %.2f°C, Outside: %.2f°C" %(mainroom["temp"],
            dungeon["temp"], now.temperature)
    bot.reply(dump)


@willie.module.interval(1)
def mqtt_update(bot):
    global client
    client.loop()
