import willie
import urllib
import status

alert = True

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
    dump = 'Total Bandwith Usage in last 24h: download: %.2fMB, upload: %.2fMB, Peak of active Devices: %d, %s' %(rx, tx, peak, people)
    bot.reply(dump)

def get_leases():
    url = "https://devlol.org/devmon/now.php"
    return int(urllib.urlopen(url))


@willie.module.interval(5*60)
def check_status(bot):
    if alert:
        status = status.query_api()
        activity = get_leases()
        if ('OPEN' in status) and (activity == 0):
            bot.msg('#devlol', 'Warnung: Der Status ist \'OPEN\' aber vermutlich keiner da!')

@willie.module.commands('alert')
def alert(bot, trigger):
    cmd = trigger.group(2)
    if cmd == 'on':
        alert = True
    elif cmd == 'off':
        alert = False
