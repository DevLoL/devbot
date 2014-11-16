#!/usr/bin/env python
# -*- coding: utf-8 -*-
import willie

commands = [
    {
        'synopsis': 'help',
        'description': 'Prints this manual.',
        'alias': ['h', 'man'],
    },
    {
        'synopsis': 'status [ OPEN | CLOSED ]',
        'description': 'Replies the current Status of the Hackerspace-API or sets it to the provided State either OPEN or CLOSED',
        'alias': ['s']
    },
    {
        'synopsis': 'weather',
        'description': 'Prints a human-readable summary of the hourly weather-data provided by forecast.io for Linz.',
        'alias': ['w'],
    },
    {
        'synopsis': 'fuckingweather',
        'description': 'Prints the fucking weather.',
        'alias': ['fw'],
    },
    {
        'synopsis': 'temp',
        'description': 'Prints current temperature and how it feels like.',
        'alias': ['t'],
    },
    {
        'synopsis': 'devmon',
        'description': 'Replies statistics of collected meta-data about our network-infrastructure.',
        'alias': ['dm', 'mon'],
    },
]

@willie.module.commands('h', 'help', 'man')
def help(bot, trigger):
    dump = ""
    dump += "=== /dev/bot manual ==="
    dump += "# Commands"
    bot.reply(dump)
