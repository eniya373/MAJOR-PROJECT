from Adafruit_IO import Client,Feed,Data
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import requests
import os

# x=ADAFRUIT_IO_USERNAME
# y=ADAFRUIT_IO_KEY
x = os.getenv('x')
y = os.getenv('y')
aio = Client(x,y)
Telegram_Token= os.getenv('Telegram_Token')

def start(bot, update):
    bot.send_message(chat_id = update.effective_chat.id, text="Welcome!")
    bot.send_message(chat_id = update.effective_chat.id, text="if you want to turn on the light then type 'Turn on the light' or if you want to turn off the light then type in 'Turn off the light'")
    
def wrong_message(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Oops!,I couldn't recognize.Please try again!!")

def send_data_to_adafruit(value1):
    value=Data(value=value1)
    value_send=aio.create_data('telebot',value)
    
def turn_on_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning on the light")
  bot.send_photo(chat_id, photo='http://scienceblog.cancerresearchuk.org/wp-content/uploads/2015/08/Lightbulb_hero2.jpg')
  send_data_to_adafruit(1)
  
def turn_off_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning off the light")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  send_data_to_adafruit(0)
  
def text_given(bot, update):
  text = update.message.text
  if text == 'Start':
    start(bot,update)
  elif text == 'Turn on the light':
    turn_on_light(bot,update)
  elif text == 'Turn off the light':
    turn_off_light(bot,update)
  else:
    wrong_message(bot,update)
    
u = Updater('Telegram_Token',use_context = True)
dip = u.dispatcher
dp.add_handler(CommandHandler('turnonthelight',turn_on_light))
dp.add_handler(CommandHandler('turnonthelight',turn_off_light))
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.command, wrong_message))
dp.add_handler(MessageHandler(Filters.text, text_given))

ud.start_polling()
ud.idle()
