
# dotdotbot: a discord bot

this bot was designed specifically to interface with a EPSON lq-1500 dot matrix printer, though it should work with any other dot matrix printer that takes direct communication.


## things to keep in mind

because of what this was developed for, it has some limitations;

- it has a hard coded line limit of 85 characters per line, that is due to the paper that we were using 
- the channel that the bot sends its startup message is also hard coded, do with that what you will.
- this was made as a proof of concept, so don't expect active development. however, if you had any ideas do feel free to open an issue.
## setup

`git clone` the repo.
`pip install` the dependincies

- discord
- python-dotenv

create a file named `.env` with the following contents, changing the values as they pertain to your setup
```.env
# discord bot token
DISCORD_TOKEN=reallylongdiscordtokenpleasereplacethis
# printer location e.g /dev/usb/lp0
PRINTER_PATH=/dev/usb/lp0
``` 
you're done! run the bot.
`python3 dotdot.py`
