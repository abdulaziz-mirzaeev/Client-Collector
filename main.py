from telegram import Update
from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import settings
updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    full_name = update.message.from_user.full_name
    update.message.reply_text("Assalomu alaykum, " + full_name + "! Botga xush kelibsiz")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()