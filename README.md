# devbot
Our irc bot based on willie (https://github.com/embolalia/willie), which tells us lots of interesting things.

## commands
* help
* devmon
* door
* temp
* weather

### help
Prints this manual.

### devmon
Replies statistics of collected meta-data about our network-infrastructure.

### door
Prints the current status of the door at /dev/lol. If locked or unlocked. Which is also displayed as prefix [OPEN] or [CLOSED] in the channels topic

### temp
Prints current temperature and how it feels like.

### weather
Prints a human-readable summary of the hourly weather-data provided by forecast.io for Linz.

## additional features
the bot periodically checks the status of devlol in the hackerspace api. If the status has changed it reports it to the channel and also keeps the topic up to date.

## legacy

* status: used to handle the manual status flag, is now replaced by more precise and automatic door_locked
