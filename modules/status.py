import willie
import urllib

laststate = ''

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
    laststate = status
    bot.say(status)

@willie.module.commands('isitChristmas')
def christmas(bot, trigger):
    bot.say('NO')

@willie.module.interval(60)
def check_status(bot):
    global laststate
    state = query_api()
    if state is not laststate:
        laststate = state
        if 'OPEN' in state:
            bot.msg('#devlol', 'the space is now OPEN')
        else:
            bot.msg('#devlol', 'the space is now CLOSED')
