import willie
import urllib
import json
import status

@willie.module.commands('door')
def door(bot, trigger):
    data = json.loads(status.query_api(mode=''))
    if data['sensors']['door_locked'][0]['value']:
        bot.reply("The door is locked!")
    else:
        bot.reply("The door is unlocked!")
