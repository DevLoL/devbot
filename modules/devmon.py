import willie
import urllib
import status

alert = True

#print info of devmon: Bandwith usage of last 24h, and lease information
@willie.module.commands('devmon')
def devmon(bot, trigger):
    url = "https://devlol.org/devmon/data/day.tsv"
    data = urllib.urlopen(url)
    rx = 0
    tx = 0
    peak = 0
    last = 0
    last_date = ''
    next(data)
    for l in data:
        args = l.split('\t')
        rx += float(args[1])
        tx += float(args[2])
        lease = int(args[3])
        if lease > peak:
            peak = lease
        if lease > 0:
            last = lease
            last_date = args[0]
    rx = (rx * 15 * 60) / 1024
    tx = (tx * 15 * 60) / 1024
    if lease > 0:
        people = '%d Devices active now' %lease
    else:
        people = 'No activity since: %s' %last_date
    dump = 'Total Bandwitdh Usage in last 24h: download: %.2fMB, upload: %.2fMB, Peak of active Devices: %d, %s' %(rx, tx, peak, people)
    bot.reply(dump)


def get_leases():
    url = "https://devlol.org/devmon/now.php"
    return int(urllib.urlopen(url).read())


#periodically check if status and devmon fit each other
@willie.module.interval(15*60)
def check_status_match(bot):
    global alert
    if alert:
        state = status.query_api()
        leases = get_leases()
        if ('OPEN' in state) and (leases == 0):
            bot.msg('#devlol', 'Warning: status is set to \'OPEN\', but no activity detected!')
            bot.msg('#devlol', '\'.status close\' or \'.alert off\'')


#this command lets you manually turn off the status alert
@willie.module.commands('alert')
def alert(bot, trigger):
    global alert
    cmd = trigger.group(2)
    if cmd == 'on':
        alert = True
    elif cmd == 'off':
        alert = False

    if alert:
        bot.say('alert is on')
    else:
        bot.say('alert is off')


#because we tend to forget toggles, alert resets every hour
@willie.module.interval(60*60)
def reset_alert(bot):
    global alert
    alert = True
