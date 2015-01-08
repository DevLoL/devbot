# devbot
Our irc bot based on willie (https://github.com/embolalia/willie), which tells us lots of interesting things.

## commands
* help
* devmon
* door
* status
* temp
* weather

### help
Prints this manual.

### devmon
Replies statistics of collected meta-data about our network-infrastructure.

### door
Prints the current status of the door at /dev/lol. If locked or unlocked.

### status
Replies the current Status of the Hackerspace-API or sets it to the provided State either OPEN or CLOSED

### temp
Prints current temperature and how it feels like.

### weather
Prints a human-readable summary of the hourly weather-data provided by forecast.io for Linz.

## additional features
the bot periodically checks the status of devlol in the hackerspace api. If the status has changed it reports it to the channel. 
