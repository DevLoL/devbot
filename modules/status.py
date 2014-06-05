import willie
import urllib

laststate = True

def query_api(mode='viewstatus'):
    url = "https://devlol.org/status/hackerspaceapi/"
    return urllib.urlopen(url + mode).read()

@willie.module.commands('status')
def status(bot, trigger):
    global laststate
    cmd = trigger.group(2)
    if cmd == 'open':
        mode = 'set/open'
    elif cmd == 'close':
        mode = 'set/close'
    else:
        mode = 'viewstatus'
    status = query_api(mode)
    laststate = 'OPEN' in status
    bot.say(status)

@willie.module.commands('isitChristmas')
def christmas(bot, trigger):
    bot.say('NO')

@willie.module.interval(60)
def check_status(bot):
    global laststate
    state = 'OPEN' in query_api()
    if laststate is not state:
        laststate = state
        if state:
            bot.msg('#devlol', 'the space is now OPEN')
        else:
            bot.msg('#devlol', 'the space is now CLOSED')

#init state on startup
laststate = 'OPEN' in query_api()
