import os
import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

def start(bot, update):
		update.message.reply_text(
        	'Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    update.message.reply_text("HEEELP")

def hello(bot, update):
		update.message.reply_text(
        	'Hello {}'.format(update.message.from_user.first_name))




    
if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "533314669:AAF_L5ViVpyyEsdy0DKK1SshUwHUQ3bQPi8"
    NAME = "tele2-bot"

    # Port is given by Heroku
    PORT = int(os.environ.get('PORT'))

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()

