import telegram

bot = telegram.Bot(token = '1796167481:AAGJGFllB3xvV95jdTv02el2')

for i in bot.getUpdates():
    print(i.message)

