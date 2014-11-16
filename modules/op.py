import willie

@willie.module.commands('op')
def op(bot, trigger):
    #bot.add_op('#test', trigger.nick)
    bot.write(('MODE',), '+o ' + trigger.nick)
