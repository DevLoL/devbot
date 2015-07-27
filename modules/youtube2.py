# -*- coding: utf8 -*-
"""
youtube.py - Willie YouTube Module
Copyright 2014, doebi
Copyright 2012, Dimitri Molenaars, Tyrope.nl.
Copyright © 2012-2013, Elad Alfassa, <elad@fedoraproject.org>
Copyright 2012, Edward Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://willie.dfbta.net

This module will respond to .yt and .youtube commands and searches the youtubes.
"""

from willie import web, tools
from willie.module import rule, commands, example
import json
import re
import requests
from HTMLParser import HTMLParser


def setup(bot):
    regex = re.compile('(youtube.com/watch\S*v=|youtu.be/)([\w-]+)')
    if not bot.memory.contains('url_callbacks'):
        bot.memory['url_callbacks'] = tools.WillieMemory()
    bot.memory['url_callbacks'][regex] = ytinfo


@rule('.*(youtube.com/watch\S*v=|youtu.be/)([\w-]+).*')
def ytinfo(bot, trigger, found_match=None):
    """
    Get information about the latest video uploaded by the channel provided.
    """
    match = found_match or trigger
    #Grab info from YT API
    uri = 'http://www.youtube.com/oembed?url=http://youtube.com/watch?v=' + match.group(2) + '&format=json'
    r = requests.get(uri)
    if not r.status_code == requests.codes['\o/']:
        return
    
    ytoembed = r.json()
    #combine variables and print
    message = '[YouTube] ' + ytoembed['title'] + \
              ' [' + ytoembed['author_name']  + ']'

    bot.say(HTMLParser().unescape(message))
