import willie
import urllib
import datetime
import json

laststate = True

def query_api(mode='viewstatus'):
    url = "https://devlol.org/status/hackerspaceapi/"
    return urllib.urlopen(url + mode).read()

def isLocked():
    data = json.loads(query_api(mode=''))
    b = data['sensors']['door_locked'][0]['value']
    return b

def isOpen():
    return not isLocked()

@willie.module.commands('fuckingstatus')
def fuckingstatus(bot, trigger):
    bot.reply("legacy command: please read the topic")

@willie.module.commands('status')
def status(bot, trigger):
    bot.reply("read the fucking topic")

@willie.module.commands('isitChristmas')
def christmas(bot, trigger):
    days_to_go = (datetime.date(datetime.date.today().year, 12, 24) - datetime.date.today()).days
    if days_to_go == 0:
        boy.say("Happy Birthday Brian!")
    else:
        bot.say("No. But it's only %i days to go." % days_to_go)

@willie.module.interval(60)
def check_status(bot):
    global laststate
    state = isOpen()
    if laststate is not state:
        # trigger the topic broadcast
        bot.write(('TOPIC', '#devlol'))
        laststate = state
        if state:
            bot.msg('#devlol', 'the space is now OPEN')
        else:
            bot.msg('#devlol', 'the space is now CLOSED')

@willie.module.rule('.*')
@willie.module.event('332')
def topic_set(bot, trigger):
    if isOpen():
        prefix = '[OPEN]'
    else:
        prefix = '[CLOSED]'
    if not trigger.startswith(prefix) or trigger.count(prefix) > 1:
        bot.write(('TOPIC', '#devlol'), prefix + " " + trigger.replace('[OPEN]', '').replace('[CLOSED]', '').strip(" "))

@willie.module.rule('.*')
@willie.module.event('TOPIC')
def topic_trigger(bot, trigger):
    bot.write(('TOPIC', '#devlol'))

@willie.module.commands('door')
def door(bot, trigger):
    bot.write(('TOPIC', '#devlol'))
    if isLocked():
        bot.reply("The door is locked!")
    else:
        bot.reply("The door is unlocked!")

#init state on startup
laststate = isOpen()
