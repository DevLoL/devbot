#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
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

def metafridge(bot, msg):
    urllib.urlopen("http://metafridge.metalab.at/cgi-bin/post_text.cgi?killmockingbird=0&effect=0&scroll_text=" + msg)

def on_message(client, bot, msg):
    try:
        if(msg.topic == "devlol/h19/dungeon/DHT21/temp"):
            dungeon["temp"] = float(msg.payload.replace('\t', ''))
        if(msg.topic == "devlol/h19/dungeon/DHT21/hum"):
            dungeon["hum"] = float(msg.payload.replace('\t', ''))
        if(msg.topic == "devlol/h19/mainroom/DHT21/temp"):
            mainroom["temp"] = float(msg.payload)
        if(msg.topic == "devlol/h19/mainroom/DHT21/hum"):
            mainroom["hum"] = float(msg.payload)
        if((msg.topic == "devlol/h19/mainroom/craftui/button/buttonHi5") and (msg.payload == "DOWN")):
            bot.msg('#devlol', 'Hi5!')
            metafridge(bot, "Hi5! Hi5! Hi5!")
        if((msg.topic == "devlol/h19/mainroom/craftui/button/button_black") and (msg.payload == "DOWN")):
            metafridge(bot, "Gruesze aus Linz!")
    except Exception, e:
        print e
        print "Error in MQTT Message."
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
def fuckingweather(bot, trigger):
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
    dump = "Mainroom: %.2f°C, Dungeon: %.2f°C, Outside: %.2f°C" %(mainroom["temp"], dungeon["temp"], now.temperature)
    bot.reply(dump)

@willie.module.commands('humidity')
def humiditiy(bot, trigger):
    forecast = forecastio.load_forecast(API_KEY, lat, lng)
    now = forecast.currently()
    dump = "Mainroom: %.2f, Dungeon: %.2f, Outside: %.2f" %(mainroom["hum"], dungeon["hum"], now.humidity*100)
    bot.reply(dump)

@willie.module.interval(1)
def mqtt_update(bot):
    global client
    if mqtt_update.init_userdata:
        mqtt_update.init_userdata = False
        client.user_data_set(bot)
    client.loop()
mqtt_update.init_userdata = True

@willie.module.commands('metafridge')
def metatrigger(bot, trigger):
    if(trigger.group(2) is not None):
        metafridge(bot, trigger.group(2))
        bot.say("Posted to Metafridge!")
    else:
        bot.reply("Add a Message.")
