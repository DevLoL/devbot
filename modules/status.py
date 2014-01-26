import willie
import urllib

def query_api(mode='viewstatus'):
    url = "https://devlol.org/status/hackerspaceapi/"
    return urllib.urlopen(url + mode)

@willie.module.commands('status')
def status(bot, trigger):
    cmd = trigger.group(2)
    if cmd == 'open':
        mode = 'set/open'
    elif cmd == 'close':
        mode = 'set/close'
    else:
        mode = 'viewstatus'
    status = query_api(mode)
    bot.say(status.read())

@willie.module.commands('isitChristmas')
def christmas(bot, trigger):
    bot.say('NO')

"""
@willie.module.interval(30)
def check_topic(bot):
    bot.write()

@willie.module.commands('topic')
def topic_test(bot, trigger):
    channel = '#test'
    topic = 'test'
    bot.write(('TOPIC', channel))

#@willie.module.rule('^[T|t]opic for #([A-z0-9.-]+) is "(.*)"$')
@willie.module.event(332)
def check_topic(bot, trigger):
    trigger.rule = '.*'
    bot.say('The topic is MINE!')
"""
