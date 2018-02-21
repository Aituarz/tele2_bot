import os
import logging
import config
import telebot
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

bot = telebot.TeleBot(config.token)
TOKEN = "533314669:AAF_L5ViVpyyEsdy0DKK1SshUwHUQ3bQPi8"
NAME = "tele2_bot"

def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)


