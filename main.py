import os
import logging
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

VOICE_PROBLEM, INTERNET_PROBLEM, FINAL = range(3)

def start(bot, update):
	try:
    keyboard = [[InlineKeyboardButton("Voice", callback_data='1'),
                 InlineKeyboardButton("Internet", callback_data='2')]]
    update.message.reply_text('Please choose your problem:', reply_markup=reply_markup)
		return FINAL
	except:
		update.message.reply_text("Please try again from /start")
		return FINAL
  
def voice(bot, update):
	try:
    keyboard = [[InlineKeyboardButton("2G", callback_data='1'),
                 InlineKeyboardButton("3G", callback_data='2')]]
    update.message.reply_text('Please choose your technology:', reply_markup=reply_markup)
		return FINAL
	except:
		update.message.reply_text("Please try again from /start")
		return FINAL
  
def internet(bot, update):
	try:
    keyboard = [[InlineKeyboardButton("2G", callback_data='1'),
                 InlineKeyboardButton("3G LTE", callback_data='2')]]
    update.message.reply_text('Please choose your technology:', reply_markup=reply_markup)
		return FINAL
	except:
		update.message.reply_text("Please try again from /start")
		return FINAL


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def done(bot, update, user_data):
    update.message.reply_text("Bye bye")
    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

    
  
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
    
    # Add handlers
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            VOICE_PROBLEM: [MessageHandler(Filters.text,
                                          voice,
                                          pass_user_data=True),
                           ],

            INTERNET_PROBLEM: [MessageHandler(Filters.text,
                                           internet,
                                           pass_user_data=True),
                            ],
            FINAL: [MessageHandler(Filters.text,
                                           voice,
                                           pass_user_data=True),
                            ],
		
        },

        fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
    )

    dp.add_handler(conv_handler)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
