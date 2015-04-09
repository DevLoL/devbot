#!/usr/bin/env python
# -*- coding: utf-8 -*-
import willie
import urllib

@willie.module.commands('metafridge')
def metafridge(bot, trigger):
    urllib.urlopen("http://metafridge.metalab.at/cgi-bin/post_text.cgi?killmockingbird=0&effect=0&scroll_text=" + trigger.group(2))
    bot.reply("Posted to Metafridge!")
