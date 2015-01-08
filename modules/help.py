#!/usr/bin/env python
# -*- coding: utf-8 -*-
import willie

commands = {
    'help': {
        'synopsis': 'help [ COMMAND ]',
        'description': 'Prints this manual.',
        'alias': ['h', 'man'],
    },
    'status': {
        'synopsis': 'status [ OPEN | CLOSED ]',
        'description': 'Replies the current Status of the Hackerspace-API or sets it to the provided State either OPEN or CLOSED',
        'alias': ['s']
    },
    'devmon': {
        'synopsis': 'devmon',
        'description': 'Replies statistics of collected meta-data about our network-infrastructure.',
        'alias': ['dm', 'mon'],
    },
    'door': {
        'synopsis': 'door',
        'description': 'Prints the current status of the door at /dev/lol. If locked or unlocked.',
        'alias': ['dm', 'mon'],
    },
    'temp': {
        'synopsis': 'temp',
        'description': 'Prints current temperature and how it feels like.',
        'alias': ['t'],
    },
    'weather': {
        'synopsis': 'weather',
        'description': 'Prints a human-readable summary of the hourly weather-data provided by forecast.io for Linz.',
        'alias': ['w'],
    },
}

@willie.module.commands('h', 'help', 'man')
def help(bot, trigger):
    cmd = trigger.group(2)
    if cmd:
        bot.say('.' + commands[cmd]['synopsis'])
        bot.say(commands[cmd]['description'])
    else:
        bot.say("=== /dev/bot manual ===")
        for k, v in sorted(commands.iteritems()):
            bot.say('.' + v['synopsis'])
