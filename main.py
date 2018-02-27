import os
import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

def start(message):
  markup = types.ReplyKeyboardMarkup(True, False)
  button1 = types.KeyBoardButton('Info')
  button2 = types.KeyBoardButton('Request')
  markup.add(button1, button2)
  
def info(info):
  update.message,reply_text(
      "ForeCast v.1.0",
      reply_markup=markup)

def request(message):
  markup = types.ReplyKeyboardMarkup(True, False)
  button1 = types.KeyBoardButton('Call')
  button2 = types.KeyBoardButton('Internet')
  markup.add(button1, button2)
 
  
if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "533314669:AAF_L5ViVpyyEsdy0DKK1SshUwHUQ3bQPi8"
    NAME = "tele2-ran"

    # Port is given by Heroku
    PORT = int(os.environ.get('PORT'))

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, start))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
