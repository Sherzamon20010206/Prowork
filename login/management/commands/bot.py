from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from telegram import Bot
from django.conf import settings
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters,\
    CallbackQueryHandler

from bot.views import *

import random
import string
import secrets












def generateRandomAlphaNumericString(length):

    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return  result_str




button = ReplyKeyboardMarkup([["Kod"]], resize_keyboard=True)

def start(update,context):
    update.message.reply_text("salom",reply_markup=button)
    return "1"

def kod(update,context):

    login=generateRandomAlphaNumericString(10)
    password=generateRandomAlphaNumericString(15)
    update.message.reply_text(f"sizning kodingiz")
    update.message.reply_text(f"login : {login}")
    update.message.reply_text(f"password : {password}")
    user = User.objects.create_user(login, 'email', password)
    user.save()




class Command(BaseCommand):
    help = 'Telegram-bot'


    def handle(self, *args, **options):
        request = Request(
            connect_timeout=None,
            read_timeout=None
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )

        updater = Updater(
            bot=bot,
            use_context=True
        )







        conv_hand = ConversationHandler(
            entry_points=[
                CommandHandler('start', start)
            ],
            states={
                '1':[MessageHandler(Filters.regex('^(' + 'Kod' + ')$'), kod)],




            },
            fallbacks=[
                CommandHandler('start', start)
            ]

        )
        updater.dispatcher.add_handler(conv_hand)
        updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members,onjoin))
        updater.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member,onleft))

        updater.start_polling()
        updater.idle()













