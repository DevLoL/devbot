import willie
import urllib
import datetime
import json

@willie.module.commands('events')
def events(bot, trigger):
    dump = urllib.urlopen("http://devlol.at/api/events").read()
    data = json.loads(dump)
    bot.reply("upcoming events:")
    for e in data['events']:
        bot.say(e['date'] + " " + e['time'] + ", " + e['title'] + " - " + e['subtitle'])
