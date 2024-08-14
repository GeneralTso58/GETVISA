# GETVISA
The script has been tested to work on ubuntu and macos using python version 3.12.3.

## Setup
### prerequisite
If you are looking into using this bot, you have most likely already filled up a DS-160 and visited https://ais.usvisa-info.com/en-ca/niv to try to set up an appointment. The wait is long. Here is how to use this bot to get an appointment.
- start **another** DS-160 application. you don't need to finish it. It suffices to get a new DS-160 number. Then you can use that number to set up **another** account here https://ais.usvisa-info.com/en-ca/niv. The point is now you have a safe account you can bot against without fear of getting banned. Please note down the user name and password of the bot account.
- apply for another gmail account and enable gmail app password. This would be the gmail the bot uses to email your personal gmail once it finds a slot.
- download chrome if you don't have it
### How to use the bot
- clone this repo.
- create a Credentials file with following fields
```
GMAIL_BOT_ADDRESS = "gmail address for bot to use"
GMAIL_APP_PASSWORD = "gmail app password for the bot"
GMAIL_PERSONAL_ADDRESS = "your personal gmail address"
CONSULATE_LOGIN_USERNAME = "login username of your bot account"
CONSULATE_LOGIN_PASSWORD = "login password of your bot account"
```
- run the command the root folder: `python3 -m venv .venv`
- then `source .venv/bin/activate`
- then `pip install -r requirements.txt`
- then `python main.py`
- you should see chrome fired up.
- adjust `isInDesiredMonthYear` function to see which month you want your appointment to be in